"""Local, account-scoped recommendation retrieval. Python standard library only."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

ACCOUNTS = ('gzminge', 'gzxzcs', 'qycslc', 'gzcktxpp', 'tsxbj', 'gzlxcs')


def connect(planning):
    cache = planning / '推荐记录' / '_retrieval.sqlite'
    cache.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(cache)
    db.executescript('''
      CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY, size INTEGER, stamp INTEGER, digest TEXT);
      CREATE TABLE IF NOT EXISTS events(id TEXT PRIMARY KEY, kind TEXT, time TEXT, batch TEXT, path TEXT, line INTEGER, data TEXT);
      CREATE TABLE IF NOT EXISTS topics(id TEXT, event TEXT, text TEXT, data TEXT, PRIMARY KEY(id,event));
    ''')
    return db


def sync(db, planning, account):
    """Read only appended bytes; verify prefix if a previously seen file changed."""
    files = sorted((planning / '推荐记录').glob('[0-9][0-9][0-9][0-9]-[0-9][0-9].jsonl'))
    known = {r[0]: r[1:] for r in db.execute('SELECT path,size,stamp,digest FROM files')}
    if set(known) - {p.name for p in files}:
        raise ValueError('Source removed; explicit cache rebuild required. Do not trust stale retrieval.')
    added = 0
    with db:
        for path in files:
            stat = path.stat()
            old = known.get(path.name)
            if old and old[:2] == (stat.st_size, stat.st_mtime_ns):
                continue
            raw = path.read_bytes()
            offset = old[0] if old else 0
            if old and hashlib.sha256(raw[:offset]).hexdigest() != old[2]:
                raise ValueError('Source edited or truncated; rebuild cache before retrieval: ' + path.name)
            if raw and not raw.endswith(b'\n'):
                raise ValueError('Incomplete JSONL line: ' + path.name)
            first_line = raw[:offset].count(b'\n') + 1
            for line, content in enumerate(raw[offset:].decode('utf-8-sig').splitlines(), first_line):
                if not content.strip():
                    continue
                event = json.loads(content)
                if event.get('account_id') != account:
                    raise ValueError('Cross-account event: ' + path.name)
                for field in ('event_id', 'event_type', 'occurred_at'):
                    if not event.get(field):
                        raise ValueError('Missing ' + field)
                packed = json.dumps(event, ensure_ascii=False, sort_keys=True)
                existing = db.execute('SELECT data FROM events WHERE id=?', (event['event_id'],)).fetchone()
                if existing:
                    if existing[0] != packed:
                        raise ValueError('Conflicting duplicate event ID')
                    continue
                db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?)', (
                    event['event_id'], event['event_type'], event['occurred_at'],
                    event.get('batch_id'), path.name, line, packed))
                for topic in event.get('topics', []):
                    text = ' '.join(str(topic.get(k, '')) for k in (
                        'title', 'audience', 'decision_question', 'core_answer', 'service'))
                    compact = {k: topic.get(k) for k in (
                        'topic_id', 'title', 'audience', 'decision_question', 'core_answer')}
                    db.execute('INSERT INTO topics VALUES(?,?,?,?)', (
                        topic['topic_id'], event['event_id'], text,
                        json.dumps(compact, ensure_ascii=False)))
                added += 1
            db.execute('INSERT OR REPLACE INTO files VALUES(?,?,?,?)', (
                path.name, len(raw), stat.st_mtime_ns, hashlib.sha256(raw).hexdigest()))
    return added


def referenced(row):
    return {'event_id': row[0], 'source': row[1], 'line': row[2], 'record': json.loads(row[3])}


def retrieve(db, mode, terms=(), limit=10, offset=0):
    if mode == 'recent':
        batches = db.execute("SELECT id,batch,data,path,line FROM events WHERE kind='recommendation' ORDER BY time DESC,id DESC LIMIT 5").fetchall()
        result, ids, batch_ids = [], set(), set()
        for eid, batch, data, path, line in batches:
            event = json.loads(data)
            ids.update(t['topic_id'] for t in event.get('topics', []))
            ids.update(event.get('replaces_topic_ids', []))
            batch_ids.add(batch)
            result.append({'event_id': eid, 'batch_id': batch, 'source': path, 'line': line,
                           'replaces_topic_ids': event.get('replaces_topic_ids', []),
                           'topics': [json.loads(r[0]) for r in db.execute('SELECT data FROM topics WHERE event=?', (eid,))]})
        # Include parent topic pointers for partial replacements, without loading whole old batches.
        parents = []
        for tid in sorted(ids):
            row = db.execute('SELECT t.data,e.path,e.line FROM topics t JOIN events e ON e.id=t.event WHERE t.id=? ORDER BY e.time DESC LIMIT 1', (tid,)).fetchone()
            if row:
                parents.append({'topic': json.loads(row[0]), 'source': row[1], 'line': row[2]})
        feedback = []
        for row in db.execute("SELECT id,path,line,data FROM events WHERE kind='feedback' ORDER BY time,id"):
            event = json.loads(row[3])
            if event.get('batch_id') in batch_ids or ids.intersection(event.get('topic_ids', [])):
                feedback.append(referenced(row))
        return {'batches': result, 'related_topics': parents, 'feedback': feedback}
    if mode == 'feedback':
        rows = db.execute("SELECT id,path,line,data FROM events WHERE kind='feedback' ORDER BY rowid LIMIT ? OFFSET ?", (limit + 1, offset)).fetchall()
        return {'items': [referenced(r) for r in rows[:limit]], 'offset': offset,
                'has_more': len(rows) > limit, 'next_offset': offset + min(len(rows), limit)}
    if not terms:
        raise ValueError('search requires --terms (space-separated concepts and synonyms)')
    matches = {}
    for row in db.execute('SELECT t.id,t.text,t.data,e.id,e.path,e.line,e.time FROM topics t JOIN events e ON e.id=t.event ORDER BY e.time DESC'):
        score = sum(term.casefold() in row[1].casefold() for term in terms)
        if score and row[0] not in matches:
            matches[row[0]] = {'topic': json.loads(row[2]), 'event_id': row[3],
                               'source': row[4], 'line': row[5], 'last_recommended': row[6], 'score': score}
    items = sorted(matches.values(), key=lambda r: (-r['score'], r['topic']['topic_id']))
    return {'items': items[offset:offset + limit], 'total': len(items),
            'has_more': len(items) > offset + limit, 'lexical_only': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--account', required=True, choices=ACCOUNTS)
    parser.add_argument('--mode', choices=('sync', 'recent', 'feedback', 'search'), default='recent')
    parser.add_argument('--terms', nargs='*', default=[])
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--offset', type=int, default=0)
    args = parser.parse_args()
    if not 1 <= args.limit <= 50 or args.offset < 0:
        parser.error('limit must be 1..50; offset must be nonnegative')
    root = Path(__file__).resolve().parents[2]
    planning = root / 'accounts' / args.account / '内容库' / '03-选题规划'
    if not planning.is_dir():
        parser.error('Account planning directory missing')
    db = connect(planning)
    try:
        added = sync(db, planning, args.account)
        output = {'added_events': added}
        if args.mode != 'sync':
            output.update(retrieve(db, args.mode, args.terms, args.limit, args.offset))
        print(json.dumps(output, ensure_ascii=False))
    finally:
        db.close()


if __name__ == '__main__':
    main()

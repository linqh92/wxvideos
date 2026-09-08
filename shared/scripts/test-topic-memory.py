"""Exercise retrieval with isolated synthetic logs; never touches account data."""
import importlib.util
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('memory', Path(__file__).with_name('topic-memory.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def run():
    with tempfile.TemporaryDirectory(prefix='topic-memory-test-') as folder:
        planning = Path(folder)
        db = m.connect(planning)
        log = planning / '推荐记录' / '2026-09.jsonl'
        def append(event):
            with log.open('a', encoding='utf-8') as f:
                f.write(json.dumps(event, ensure_ascii=False) + '\n')
        for i in range(8):
            append(dict(event_id=f'e{i}', event_type='recommendation', account_id='gzminge',
                        occurred_at=f'2026-09-0{i+1}T10:00:00+08:00', batch_id=f'b{i}',
                        replaces_topic_ids=['t0'] if i == 7 else [],
                        topics=[dict(topic_id=f't{i}', title=f'题{i}', decision_question='旧题资格' if i == 0 else '问题', core_answer='条件')]))
        assert m.sync(db, planning, 'gzminge') == 8
        assert m.sync(db, planning, 'gzminge') == 0
        recent = m.retrieve(db, 'recent')
        assert len(recent['batches']) == 5
        assert any(r['topic']['topic_id'] == 't0' for r in recent['related_topics'])
        assert m.retrieve(db, 'search', ['资格'])['items'][0]['topic']['topic_id'] == 't0'
        for i, signal in enumerate(['reject', 'reinstate']):
            append(dict(event_id=f'f{i}', event_type='feedback', account_id='gzminge',
                        occurred_at='2026-09-09T10:00:00+08:00', batch_id='b0', topic_ids=['t0'],
                        signal=signal, scope='topic', scope_description='仅这题', user_text=signal))
        assert m.sync(db, planning, 'gzminge') == 2
        page = m.retrieve(db, 'feedback', limit=1)
        assert page['has_more'] and page['next_offset'] == 1
        assert m.retrieve(db, 'feedback', limit=1, offset=1)['items'][0]['record']['signal'] == 'reinstate'
        assert len(m.retrieve(db, 'recent')['feedback']) == 2
        before = db.execute('SELECT COUNT(*) FROM events').fetchone()[0]
        append(dict(event_id='bad', event_type='feedback', account_id='gzxzcs', occurred_at='now'))
        try:
            m.sync(db, planning, 'gzminge')
            raise AssertionError('cross-account accepted')
        except ValueError:
            pass
        assert db.execute('SELECT COUNT(*) FROM events').fetchone()[0] == before
        log.write_text('{}\n', encoding='utf-8')
        try:
            m.sync(db, planning, 'gzminge')
            raise AssertionError('source rewrite accepted')
        except ValueError:
            pass
        db.close()
    print('PASS: recent bounds, old-topic search, partial replacement, incremental sync, feedback paging, account isolation, source mutation')


if __name__ == '__main__':
    run()

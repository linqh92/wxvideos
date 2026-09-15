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

        history_root = Path(folder) / 'accounts' / 'gzminge' / '内容库' / '01-历史内容'
        history_root.mkdir(parents=True)
        text_paths = [
            'accounts/gzminge/内容库/01-历史内容/2026-09-10｜短文一.md',
            'accounts/gzminge/内容库/01-历史内容/2026-09-12｜短文二.md',
        ]
        spoken_path = 'accounts/gzminge/内容库/01-历史内容/2026-09-11｜口播一.md'
        for path in text_paths + [spoken_path]:
            target = Path(folder).joinpath(*path.split('/'))
            target.write_text('---\nstatus: published\n---\n', encoding='utf-8')
        for event_id, occurred_at, content_format, history_path, results, limits in (
            ('p0', '2026-09-10T10:00:00+08:00', 'text_broadcast', text_paths[0],
             {'views': 1000}, 'Only an engagement signal; no causal attribution.'),
            ('p1', '2026-09-11T10:00:00+08:00', 'spoken', spoken_path,
             {'valid_consultations': 1}, 'Single published piece.'),
            ('p2', '2026-09-12T10:00:00+08:00', 'text_broadcast', text_paths[1],
             {'valid_consultations': 2}, 'Reported result; expression-level cause is unknown.'),
        ):
            append(dict(event_id=event_id, event_type='performance', account_id='gzminge',
                        occurred_at=occurred_at, topic_ids=['t0'], content_format=content_format,
                        history_path=history_path, observation_window='7d', source='user_reported',
                        results=results, attribution_limits=limits))
        assert m.sync(db, planning, 'gzminge') == 3
        performance = m.retrieve(
            db, 'performance', limit=1, account='gzminge',
            content_format='text_broadcast', repo_root=Path(folder)
        )
        assert performance['total'] == 2 and performance['has_more']
        assert performance['items'][0]['event_id'] == 'p2'
        assert performance['items'][0]['content_format'] == 'text_broadcast'
        assert performance['items'][0]['attribution_limits'] == limits
        assert Path(folder).joinpath(*performance['items'][0]['history_path'].split('/')).is_file()
        second = m.retrieve(
            db, 'performance', limit=1, offset=1, account='gzminge',
            content_format='text_broadcast', repo_root=Path(folder)
        )
        assert second['items'][0]['event_id'] == 'p0' and not second['has_more']
        assert all(item['event_id'].startswith('p') for item in performance['items'] + second['items'])
        assert len(m.retrieve(db, 'recent')['batches']) == 5
        assert len(m.retrieve(db, 'recent')['feedback']) == 2

        empty = m.connect(Path(folder) / 'empty')
        try:
            no_performance = m.retrieve(
                empty, 'performance', account='gzminge',
                content_format='text_broadcast', repo_root=Path(folder)
            )
            assert no_performance['items'] == [] and no_performance['total'] == 0
        finally:
            empty.close()

        before = db.execute('SELECT COUNT(*) FROM events').fetchone()[0]
        append(dict(event_id='bad', event_type='performance', account_id='gzxzcs',
                    occurred_at='2026-09-13T10:00:00+08:00', topic_ids=['t0'],
                    content_format='text_broadcast', history_path=text_paths[0],
                    observation_window='7d', source='user_reported', results={'views': 1},
                    attribution_limits='Cross-account fixture must be rejected.'))
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
    print('PASS: recent/search/feedback compatibility, performance filtering and paging, path validation, account isolation, source mutation')


if __name__ == '__main__':
    run()

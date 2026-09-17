#!/usr/bin/env python3
"""Read-only incumbent-v3 identity check; does not select study authority."""
import argparse
import copy
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / 'evaluation'
FREEZE = '98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab'
FILE_SHA = '34a399cda8ca9f1b07b9fa0ddad36ac4f5073ef12d8b12df42fb023818508b27'
SELF_SHA = 'b925797fcab50b2008ad5974590e323f772e5ea7013efa84ce7606007439aeb3'
WRAPPER = {'benchmark_id', 'version', 'policy_sha256', 'freeze', 'benchmark_sha256', 'compatibility_import'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def semantic(document):
    value = copy.deepcopy(document)
    for key in WRAPPER:
        value.pop(key, None)
    for row in value['relationships']:
        if 'type' in row:
            assert 'relationship_type' not in row
            row['relationship_type'] = row.pop('type')
    return value


def inspect(repository):
    def blob(path):
        return subprocess.check_output(['git', '-C', str(repository), 'show', f'{FREEZE}:{path}'])
    frozen_bytes = blob('source/source-benchmark.v3.json')
    local_bytes = (EV / 'import/legacy-benchmark-v3/source/source-benchmark.v3.json').read_bytes()
    assert digest(frozen_bytes) == FILE_SHA and local_bytes == frozen_bytes
    original = json.loads(frozen_bytes)
    assert original['benchmark_sha256'] == SELF_SHA
    canonical = {k:v for k,v in original.items() if k != 'benchmark_sha256'}
    assert digest(json.dumps(canonical, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) == SELF_SHA
    current_path = EV / 'source/source-benchmark.v4.json'
    current = json.loads(current_path.read_text())
    assert semantic(original) == semantic(current), 'Benchmark semantic content changed'
    structure = json.loads(next((EV / 'candidates').rglob('structure-audit.v6.json')).read_text())
    density = []
    for row in structure['density']['chapter_measurements']:
        name = f"source/source-subject-chunk.{row['chunk_id']}.json"
        payload = blob(name)
        words = json.loads(payload)['page_review']['indexable_source_words']
        assert words == row['indexable_source_words'], row['chunk_id']
        density.append({'chunk_id':row['chunk_id'], 'discovery_path':name, 'discovery_file_sha256':digest(payload), 'indexable_source_words':words})
    assert len(density) == 17
    state = json.loads((EV / 'evaluation-state.json').read_text())
    for artifact in state['artifacts']:
        assert digest((EV / artifact['path']).read_bytes()) == artifact['sha256'], artifact['path']
    return {'status':'incumbent_identity_inspection_only_selection_pending', 'selection_status':'Await candidate-blind comparison and choice among v3, native, or reviewed v4; identity is not a quality judgment.', 'incumbent_release':FREEZE,
            'incumbent_file_sha256':FILE_SHA, 'incumbent_self_hash':SELF_SHA,
            'current_file_sha256':digest(current_path.read_bytes()), 'current_self_hash':current['benchmark_sha256'],
            'semantic_identity':True, 'wrapper_fields_excluded':sorted(WRAPPER),
            'only_semantic_normalization':'relationships[*].type -> relationship_type',
            'semantic_sha256':digest(json.dumps(semantic(current),sort_keys=True,separators=(',', ':'),ensure_ascii=False).encode()),
            'subjects':len(current['subjects']), 'reader_tasks':len(current['reader_tasks']),
            'relationships':len(current['relationships']), 'density_basis':density,
            'density_source_words':sum(r['indexable_source_words'] for r in density),
            'registered_artifact_hashes_verified':len(state['artifacts']),
            'original_freeze_preserved':original['freeze'], 'current_freeze_preserved':current['freeze']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--benchmark-repository', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(inspect(args.benchmark_repository), indent=2, ensure_ascii=False))

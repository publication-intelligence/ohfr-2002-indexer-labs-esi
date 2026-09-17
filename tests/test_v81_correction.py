"""Regression checks for the authorized targeted correction and current bundle."""
import hashlib
import json
import subprocess
import sys
import unittest
from decimal import localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / 'evaluation'
BASE = 'b9c2fa4'
SKILL = Path.home() / '.codex/skills/evaluate-subject-index/scripts'
sys.path.insert(0, str(SKILL))
sys.path.insert(0, str(ROOT / 'scripts'))
import dimension_score_v8_cli as scoring
import web_projection
from project_v81_review_signals import supplemental_signal


def load(path):
    return json.loads(path.read_text())


def historical(path):
    return json.loads(subprocess.check_output(['git', 'show', f'{BASE}:{path.relative_to(ROOT)}'], cwd=ROOT))


class V81CorrectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = load(EV / 'evaluation-state.json')
        cls.candidate_dir = EV / Path(cls.state['candidate']['normalized_path']).parent
        cls.score_dir = EV / Path(next(a['path'] for a in cls.state['artifacts'] if a['artifact_type'] == 'dimension_calculations')).parent
        cls.calculation = load(cls.score_dir / 'dimension-calculations.v6.json')
        cls.result = load(cls.score_dir / 'evaluation-result.v12.json')
        cls.structure = load(cls.candidate_dir / 'structure-audit.v6.json')

    def test_exactly_one_delivered_record_is_corrected(self):
        p = self.candidate_dir / 'candidate-index.v2.json'
        old, new = historical(p), load(p)
        changed = [(a, b) for a, b in zip(old['records'], new['records']) if a != b]
        self.assertEqual(1, len(changed))
        a, b = changed[0]
        self.assertEqual(a['record_id'], b['record_id'])
        self.assertEqual('Senez, see of, 143', b['original_displayed_form'])
        self.assertEqual(['Senez, see of'], b['heading_path'])
        self.assertEqual([], b['cross_references'])
        self.assertEqual(143, b['locator_assignments'][0]['document_page'])
        self.assertEqual('LOC-9FE249AA2E90', b['locator_assignments'][0]['locator_id'])

    def test_original_locator_judgments_are_unchanged(self):
        added = []
        for p in sorted((self.candidate_dir / 'locator-audits').glob('*.json')):
            old, new = historical(p), load(p)
            before = {x['locator_id']: x for x in old['judgments']}
            after = {x['locator_id']: x for x in new['judgments']}
            self.assertTrue(before.keys() <= after.keys())
            for key, value in before.items():
                self.assertEqual(value, after[key])
            added.extend(after[key] for key in after.keys() - before.keys())
        self.assertEqual(1, len(added))
        self.assertEqual(('supported', 'substantive', 'exact_fit'),
                         tuple(added[0][k] for k in ('judgment', 'treatment_class', 'complete_path_fit')))

    def test_missing_access_and_benchmark_content_are_reused(self):
        for p in sorted((self.candidate_dir / 'missing-access-audits').glob('*.json')):
            old, new = historical(p), load(p)
            old.pop('benchmark_sha256'); new.pop('benchmark_sha256')
            self.assertEqual(old, new)
        p = EV / 'source/source-benchmark.v4.json'
        old, new = historical(p), load(p)
        for key in ('policy_sha256', 'benchmark_sha256'):
            old.pop(key); new.pop(key)
        self.assertEqual(old, new)

    def test_all_registered_local_bytes_and_exact_inputs_match(self):
        for record in self.state['artifacts']:
            p = EV / record['path']
            if record['visibility'] == 'restricted' and not p.exists():
                continue
            self.assertEqual(record['sha256'], hashlib.sha256(p.read_bytes()).hexdigest(), str(p))
        p = self.score_dir / 'dimension-calculation-input.v2.json'
        # The historical projection test module sets process-wide precision to
        # 50; isolate the current CLI's standard Decimal precision of 28.
        with localcontext() as context:
            context.prec = 28
            calculation = scoring.calculate_loaded(scoring.load_v8_inputs(p))
        self.assertEqual(self.calculation, calculation)
        self.assertEqual(85.12, calculation['overall_percentage'])

    def test_consequences_and_review_signals(self):
        self.assertEqual('valid', self.result['evaluation_validity']['status'])
        self.assertEqual({'GATE-WRONG-LOCATOR', 'GATE-BROKEN-REFERENCE'}, {g['gate_id'] for g in self.result['critical_gates'] if g['triggered']})
        caps = [c for d in self.calculation['dimensions'] for c in d['cap_evaluations'] if c['triggered']]
        self.assertEqual({'coverage.essential_miss_rate', 'reliability.distributed_unsupported_pattern'}, {c['cap_id'] for c in caps})
        self.assertTrue(all(d['dimension_percentage'] == d['pre_cap_percentage'] for d in self.calculation['dimensions']))
        signal = supplemental_signal(self.structure)
        self.assertEqual(70, signal['count'])
        self.assertIn(signal, self.result['review_signals'])
        partial = next(s for s in self.result['review_signals'] if s['signal_id'] == 'REVIEW-PARTIAL-FIT')
        self.assertEqual((71, 'yellow', False), (partial['count'], partial['color'], partial['individually_caps_or_gates']))

    def test_full_current_public_bundle(self):
        root = self.score_dir / 'v8-canonical-projection'
        projection = load(root / 'projection.v1.json')
        collections = {key: load(root / path) for key, path in web_projection.COLLECTION_PATHS.items() if (root / path).exists()}
        web_projection.validate_bundle(projection, collections)
        report = load(self.score_dir / 'web-report.v10.json')
        scoring.core.validate_schema_document(report, 'web-report-v10.schema.json', 'Current report')
        self.assertEqual(6, len(report['calculation_explainer']['dimension_denominators']))
        self.assertEqual(self.result['review_signals'], projection['review_signals'])
        self.assertEqual({'records':1644, 'heading_nodes':1644, 'paths':1644, 'displayed_locators':5056, 'atomic_locators':6222, 'cross_references':10}, collections['index_records']['counts'])
        self.assertEqual(194718, sum(x['indexable_source_words'] for x in collections['density']['items']))

    def test_supplemental_findings_never_become_major_without_an_independent_cause(self):
        for node in self.structure['node_judgments']:
            access = node['component_judgments']['heading_access_architecture']
            findings = access.get('causal_findings', [])
            for finding in findings:
                if finding['kind'] == 'benchmark_access':
                    self.assertEqual('minor', finding['severity'])
            if access['status'] in ('major_issues', 'fails'):
                self.assertTrue(any(f['kind'] != 'benchmark_access' and f['severity'] in ('major', 'critical') for f in findings))


if __name__ == '__main__':
    unittest.main()

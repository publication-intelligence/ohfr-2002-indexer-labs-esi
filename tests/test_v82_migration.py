"""V8.2 reuses the corrected checkpoint: only provenance and gates change."""
import copy
import hashlib
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / 'evaluation'
BASE = '48bb67b434335cd90002f7bf2078a8a176e2a525'


def load(p):
    return json.loads(p.read_text())


def old(p):
    return json.loads(subprocess.check_output(['git', 'show', f'{BASE}:{p.relative_to(ROOT)}'], cwd=ROOT))


class V82MigrationTests(unittest.TestCase):
    def test_every_numeric_component_and_cap_is_invariant(self):
        before = load(EV / 'scoring-v81/dimension-calculations.v6.json')
        after = load(EV / 'scoring-v82/dimension-calculations.v6.json')
        for key in ('overall_percentage', 'maximum_percentage', 'final_rounding', 'arithmetic_check', 'diagnostic_item_grades'):
            self.assertEqual(before[key], after[key], key)
        for a, b in zip(before['dimensions'], after['dimensions']):
            a, b = copy.deepcopy(a), copy.deepcopy(b)
            # Versioned formula names and evidence bindings change; all remaining
            # fields include every denominator, component, deduction and cap.
            for key in ('formula_id', 'input_artifacts'):
                a.pop(key); b.pop(key)
            self.assertEqual(a, b)

    def test_frozen_judgments_and_repair_are_preserved(self):
        state = load(EV / 'evaluation-state.json')
        c = EV / Path(state['candidate']['normalized_path']).parent
        for name in ('candidate-index.v2.json', 'candidate-layout-extraction.v1.json', 'item-inventory.v2.json'):
            self.assertEqual(old(c / name), load(c / name))
        for p in (c / 'locator-audits').glob('*.json'):
            self.assertEqual(old(p), load(p))
        for p in (c / 'missing-access-audits').glob('*.json'):
            a, b = old(p), load(p)
            a.pop('benchmark_sha256'); b.pop('benchmark_sha256')
            self.assertEqual(a, b)
        p = c / 'structure-audit.v6.json'
        a, b = old(p), load(p)
        for row in b['cross_reference_judgments']:
            resolution = row.pop('target_resolution')
            self.assertEqual('no_valid_destination', resolution['status'])
            self.assertEqual([], resolution['resolved_path_ids'])
            self.assertEqual(row['evidence_ids'], resolution['evidence_ids'])
        self.assertEqual(a, b)

    def test_original_and_actual_migration_provenance(self):
        p = load(EV / 'source/evaluation-policy.v4.json')
        m = p['retrospective_migration']
        self.assertTrue(p['freeze']['candidate_seen'])
        self.assertFalse(m['original_policy']['freeze']['candidate_seen'])
        self.assertEqual(m['migrated_at'], p['freeze']['frozen_at'])
        root = EV / 'migration-v8.2'
        refs = [m['original_policy']['artifact']] + [r for stage in m['reused_stages'].values() for r in stage['evidence']]
        for r in refs:
            self.assertEqual(r['sha256'], hashlib.sha256((root / r['path']).read_bytes()).hexdigest())
        self.assertTrue(all(not s['rerun'] for s in m['reused_stages'].values()))
        self.assertEqual(old(EV / 'source/evaluation-policy.v4.json'), load(root / 'preserved/v81-policy.v4.json'))

    def test_direct_gates_exclude_partial_fit_and_preserved_uncertainties(self):
        state = load(EV / 'evaluation-state.json')
        c = EV / Path(state['candidate']['normalized_path']).parent
        s = load(c / 'structure-audit.v6.json')
        uncertain = {i for u in s['uncertainties'] for i in u['affected_item_ids']}
        rows = [row for p in (c / 'locator-audits').glob('*.json') for row in load(p)['judgments']]
        expected = {r['locator_id'] for r in rows if r['judgment'] == 'unsupported' and r['complete_path_fit'] == 'no_fit' and not ({r['locator_id'], r['path_id']} & uncertain) and r['confidence'] in ('high', 'medium') and r['source_scope_status'] in ('indexable', 'excluded') and r['treatment_class'] != 'unavailable' and r['evidence_ids'] and r['fit_rationale'].strip()}
        result = load(EV / 'scoring-v82/evaluation-result.v12.json')
        gates = {g['gate_id']: g for g in result['critical_gates'] if g['triggered']}
        self.assertEqual(expected, set(gates['GATE-WRONG-LOCATOR']['affected_evidence_ids']))
        self.assertEqual(87, len(expected))
        self.assertEqual({'XREF-1FB84F43D7ED', 'XREF-80B3F994D3ED'}, set(gates['GATE-BROKEN-REFERENCE']['affected_evidence_ids']))
        self.assertEqual('indeterminate', result['gate_assessment']['status'])
        self.assertEqual(2680, len(result['gate_assessment']['blockers']))
        self.assertEqual('valid', result['evaluation_validity']['status'])
        projection = load(EV / 'scoring-v82/v8-canonical-projection/projection.v1.json')
        self.assertEqual('not_publication_ready', projection['score_views']['views'][0]['readiness']['status'])


if __name__ == '__main__':
    unittest.main()

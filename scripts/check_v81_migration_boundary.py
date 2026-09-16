#!/usr/bin/env python3
"""Verify the bounded migration report cannot silently replace frozen evidence."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text())


def main():
    ledger = load("evaluation/migration-v8.1/change-ledger.json")
    expected_self_hash = ledger.pop("ledger_content_sha256")
    canonical = json.dumps(ledger, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(canonical).hexdigest() == expected_self_hash
    assert ledger["status"] == "bounded_report_only_migration_withheld"
    assert ledger["revised_authoritative_score"] is None
    assert not ledger["new_policy_frozen_in_canonical_state"]
    validation_path = ROOT / "evaluation/migration-v8.1" / ledger["validation_results"]["path"]
    assert hashlib.sha256(validation_path.read_bytes()).hexdigest() == ledger["validation_results"]["sha256"]
    for row in ledger["delivery_file_hashes"]:
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"]
    for row in ledger["preserved_artifact_hashes"]:
        actual = hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest()
        assert actual == row["before_sha256"] == row["after_sha256"], row["path"]
    for row in ledger["exact_original_calculation_inputs"]:
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"]
    state = load("evaluation/evaluation-state.json")
    assert state["configuration"]["policy_profile"] == "subject-index-standard-policy-v8"
    candidate = load("evaluation/" + state["candidate"]["normalized_path"])
    senez = next(r for r in candidate["records"] if r["record_id"] == "REC-95178351D043")
    assert senez["original_displayed_form"] == "Senez, see of, 143"
    assert not senez["locator_assignments"]
    assert senez["cross_references"][0]["target"] == "of, 143"
    structure_record = next(a for a in state["artifacts"] if a.get("schema_version") == "structure-audit-v6")
    structure = load("evaluation/" + structure_record["path"])
    assert any(u["uncertainty_id"] == "UNCERTAINTY-SENEZ-LEXICAL-SEE" for u in structure["uncertainties"])
    original = load("evaluation/scoring/dimension-calculations.v6.json")
    assert original["overall_percentage"] == ledger["original_score"] == 77.4
    diagnostic = ledger["conditional_policy_only_diagnostic"]
    assert not diagnostic["authoritative"] and diagnostic["not_a_migration_result"]
    assert diagnostic["ordinary_pre_cap_values_unchanged"]
    assert {g["gate_id"] for g in diagnostic["triggered_gates"]} == {"GATE-SEE-SUBSTITUTION"}
    print(json.dumps({"ok": True, "unchanged_files": len(ledger["preserved_artifact_hashes"]),
                      "exact_calculation_inputs": len(ledger["exact_original_calculation_inputs"]),
                      "authoritative_v81_score": None, "senez_attribution_gap_preserved": True}))


if __name__ == "__main__":
    main()

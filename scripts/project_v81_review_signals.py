#!/usr/bin/env python3
"""Project native supplemental-route findings before the registered report build.

The V8.1 runtime's standard signal projection reads structured defects, but this
evaluation stores supplemental omissions in source-linked native node findings.
This score-free supplement preserves their yellow review signal without making
new arithmetic defects or asserting a systemic root cause.
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

SKILL = Path.home() / ".codex/skills/evaluate-subject-index/scripts"
sys.path.insert(0, str(SKILL))
import scoring_core as core
from state_cli import artifact_id, evaluation_mutation_lock, now, save_state

ROOT = Path(__file__).resolve().parents[1] / "evaluation"


def supplemental_signal(structure):
    ids = sorted({sid for node in structure["node_judgments"]
                  for finding in node["component_judgments"]["heading_access_architecture"].get("causal_findings", [])
                  if finding["kind"] == "benchmark_access" and finding["severity"] == "minor"
                  for sid in finding["source_ids"] if sid.startswith("SUBJ-")})
    return {
        "signal_id": "REVIEW-MISSING-SUPPLEMENTAL-ROUTE", "color": "yellow",
        "affected_evidence_ids": ids, "count": len(ids),
        "reason": "Source-linked native heading-access findings identify missing supplemental routes despite partial supported access. Coverage and access deductions remain; these findings do not individually cap or gate.",
        "individually_caps_or_gates": False,
    }


def main():
    state_path = ROOT / "evaluation-state.json"
    with evaluation_mutation_lock(state_path):
        state = json.loads(state_path.read_text())
        records = {row["artifact_type"]: row for row in state["artifacts"]}
        def read(kind):
            record = records[kind]
            data = (ROOT / record["path"]).read_bytes()
            assert hashlib.sha256(data).hexdigest() == record["sha256"], kind
            return json.loads(data)
        structure, metadata, result = (read(k) for k in ("structure_audit", "projection_metadata", "evaluation_result"))
        signal = supplemental_signal(structure)
        if signal in metadata["review_signals"] and metadata["review_signals"] == result["review_signals"]:
            print(json.dumps({"ok": True, "changed": False, "supplemental_subjects": signal["count"]}))
            return
        assert state["stages"]["scoring"]["status"] == "completed"
        assert state["stages"]["web_report"]["status"] == "not_started", "Project signals before building the report."
        metadata["review_signals"] = [s for s in metadata["review_signals"] if s["signal_id"] != signal["signal_id"]] + [signal]
        metadata["projection_metadata_sha256"] = core.canonical_hash(metadata, "projection_metadata_sha256")
        def payload(document):
            return (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode()
        meta_bytes = payload(metadata)
        old_hash = records["projection_metadata"]["sha256"]
        new_hash = hashlib.sha256(meta_bytes).hexdigest()
        result["review_signals"] = copy.deepcopy(metadata["review_signals"])
        result["projection_metadata"]["sha256"] = new_hash
        result["projection_metadata"]["projection_metadata_sha256"] = metadata["projection_metadata_sha256"]
        core.validate_schema_document(metadata, "v8-projection-metadata-v2.schema.json", "Metadata")
        core.validate_schema_document(result, "evaluation-result-v12.schema.json", "Result")
        for kind, data in (("projection_metadata", meta_bytes), ("evaluation_result", payload(result))):
            record = records[kind]
            record["sha256"] = hashlib.sha256(data).hexdigest()
            record["artifact_id"] = artifact_id(record["path"], record["sha256"])
            record["recorded_at"] = now()
            record["input_sha256"] = sorted(new_hash if h == old_hash else h for h in record["input_sha256"])
            (ROOT / record["path"]).write_bytes(data)
        state["updated_at"] = now()
        save_state(state_path, state)
        print(json.dumps({"ok": True, "changed": True, "supplemental_subjects": signal["count"], "arithmetic_changed": False}))


if __name__ == "__main__":
    main()

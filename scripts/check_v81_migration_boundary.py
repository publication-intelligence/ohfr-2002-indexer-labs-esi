#!/usr/bin/env python3
"""Verify the historical bounded review against its preserved Git snapshots.

The authorized follow-up now changes current evidence. The original review's
before/after labels are therefore checked at its frozen commits, not against
current V8.1 files.
"""
import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW_COMMIT = "b9c2fa4"


def verify_archive(revision, expected):
    process = subprocess.Popen(["git", "archive", revision], cwd=ROOT, stdout=subprocess.PIPE)
    seen = set()
    with tarfile.open(fileobj=process.stdout, mode="r|") as archive:
        for member in archive:
            if member.name in expected:
                actual = hashlib.sha256(archive.extractfile(member).read()).hexdigest()
                assert actual == expected[member.name], member.name
                seen.add(member.name)
    assert process.wait() == 0 and seen == set(expected)


def main():
    path = "evaluation/migration-v8.1/change-ledger.json"
    ledger = json.loads(subprocess.check_output(["git", "show", f"{REVIEW_COMMIT}:{path}"], cwd=ROOT))
    digest = ledger.pop("ledger_content_sha256")
    canonical = json.dumps(ledger, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    assert hashlib.sha256(canonical).hexdigest() == digest
    assert ledger["status"] == "bounded_report_only_migration_withheld"
    assert ledger["revised_authoritative_score"] is None
    originals = {row["path"]: row["before_sha256"] for row in ledger["preserved_artifact_hashes"]}
    verify_archive(ledger["baseline_commit"], originals)
    verify_archive(REVIEW_COMMIT, {row["path"]: row["sha256"] for row in ledger["delivery_file_hashes"]})
    print(json.dumps({"ok": True, "historical_files_verified": len(originals),
                      "current_v81_files_are_separate": True, "review_commit": REVIEW_COMMIT}))


if __name__ == "__main__":
    main()

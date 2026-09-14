"""Regression tests for the IndexerLabs V8 public web projection."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_v8_web_projection as builder  # noqa: E402

OUTPUT = ROOT / "web/v8-canonical-projection"


def load(relative: str) -> dict:
    return json.loads((OUTPUT / relative).read_text(encoding="utf-8"))


class V8WebProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.projection = builder.validate_projection_output(OUTPUT)

    def test_canonical_score_views_and_overlay_applicability(self) -> None:
        self.assertEqual(77.4, self.projection["score_views"]["views"][0]["score"])
        self.assertEqual("canonical_as_delivered", self.projection["view_selection"]["default_display_view_id"])
        self.assertEqual("not_applicable", self.projection["score_views"]["projection_adjustment_status"])
        self.assertFalse(self.projection["correction_outcomes"]["applicable"])
        self.assertFalse((OUTPUT / "data/correction-overlay.v1.json").exists())

    def test_complete_index_and_evidence_joins(self) -> None:
        records = load("data/index-records.v1.json")
        self.assertEqual({"records": 1644, "heading_nodes": 1644, "paths": 1644, "displayed_locators": 5055, "atomic_locators": 6221, "cross_references": 11}, records["counts"])
        self.assertEqual(list(range(1644)), [row["delivered_order"] for row in records["items"]])
        atomic = [item for row in records["items"] for display in row["displayed_locators"] for item in display["atomic_locators"]]
        self.assertEqual(6221, len({row["locator_id"] for row in atomic}))
        self.assertTrue(all(row["assessment"]["popover"] for row in atomic))
        self.assertTrue(all(display["atomic_locator_ids"] == [row["locator_id"] for row in display["atomic_locators"]] for record in records["items"] for display in record["displayed_locators"]))

    def test_missing_access_tasks_and_treatments_are_complete(self) -> None:
        subjects = load("data/source-subjects.v1.json")
        self.assertEqual({"source_subjects": 1366, "reader_tasks": 1026, "expected_treatments": 3210}, subjects["counts"])
        tasks = {task["task_id"] for row in subjects["items"] for task in row["reader_tasks"]}
        self.assertEqual(1026, len(tasks))
        self.assertTrue(all(task["result"] for row in subjects["items"] for task in row["reader_tasks"]))
        self.assertTrue(all(item["source_page_label"] for row in subjects["items"] for item in row["expected_treatments"]))

    def test_density_and_structure_drilldown(self) -> None:
        density = load("data/density.v1.json")
        self.assertEqual(17, density["count"])
        self.assertEqual(194718, sum(row["indexable_source_words"] for row in density["items"]))
        self.assertTrue(all(row["title"] and row["canonical_fit_judgment"]["combined"] for row in density["items"]))

    def test_hashes_bindings_and_public_safety(self) -> None:
        builder.privacy_scan(OUTPUT)
        self.assertEqual(3, len(self.projection["collections"]))
        for binding in self.projection["collections"]:
            value = load(binding["artifact_path"])
            self.assertEqual(binding["content_sha256"], value["collection_sha256"])
        text = "\n".join(path.read_text(encoding="utf-8") for path in OUTPUT.rglob("*.json"))
        self.assertNotIn('"evidence_summary"', text)
        self.assertNotIn('"private_evidence"', text)
        self.assertEqual({"source_excerpts_included": False, "restricted_files_included": False, "private_layout_evidence_included": False, "absolute_paths_included": False, "source_subject_summaries_are_synthesized_not_quoted": True}, self.projection["public_safety"])


if __name__ == "__main__":
    unittest.main()

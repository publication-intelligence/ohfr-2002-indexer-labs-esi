# V8 canonical web projection

This directory is the deterministic, public-safe web-data bundle for the completed IndexerLabs evaluation. The committed V12 result and V10 report remain authoritative.

## Canonical view and correction policy

- `canonical_as_delivered` is the authoritative, primary, and default display view.
- Its percentage-native score is **77.40/100**.
- No separately attested IndexerLabs representation correction applies. Therefore `data/correction-overlay.v1.json` is intentionally absent and the projection records the overlay as not applicable.
- The canonical gates and color tokens are passed through without reinterpretation.

## Files

- `projection.v1.json` — scorecard, gates/readiness, item summaries, provenance, collection bindings, correction applicability, and the 194,718-word density denominator.
- `data/index-records.v1.json` — all 1,644 records in delivered order, hierarchy, 5,055 displayed locators, 6,221 atomic locator mappings, 11 cross-references, causal access findings, grades, and popovers.
- `data/source-subjects.v1.json` — all 1,366 source-subject assessments, 1,026 reader tasks, and 3,210 expected-treatment records.
- `data/density.v1.json` — all 17 named chapter/intellectual-unit measurements and canonical fit judgments.
- `projection.schema.json` and `collection.schema.json` — Draft 2020-12 validation contracts.

Every generated JSON artifact has a canonical-JSON self-hash. The projection additionally binds byte hashes for every collection and canonical source artifact used by the builder.

## Regenerate and validate

```bash
python3 scripts/build_v8_web_projection.py build
python3 scripts/build_v8_web_projection.py validate
python3 -m unittest tests.test_v8_web_projection -v
git diff --check
```

## Public-safety boundary

The bundle excludes source excerpts, PDFs, absolute filesystem paths, private layout evidence, secrets, and restricted inputs. It retains synthesized source-subject descriptions, evidence identities, page labels, judgments, explanations, grades, and popovers needed by the web interface.

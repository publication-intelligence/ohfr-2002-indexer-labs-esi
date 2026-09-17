# Subject Index Evaluation: IndexerLabs / The Oxford History of the French Revolution (2002)

The current evaluation uses **V8.2** and scores **85.12%**, unchanged from the
corrected V8.1 checkpoint. Evaluation validity is valid; publication readiness
is **not ready**. Two direct gates identify 140 confirmed wrong locators and two
broken cross-references. Assessment remains indeterminate for 970 explicitly
identified uncertain locators. These gaps are not additional candidate defects.
Both 90% dimension ceilings remain non-binding. The final runtime is reviewed
revision `c11c6ccb16000fe79646af16b7be01f6cbeeac78`.
Website deployment and evaluation PR merge require user approval.

## Current artifacts

- [Final scoped-uncertainty migration](evaluation/migration-v8.2-final/REPORT.md)
- [Final validation and invariance receipt](evaluation/migration-v8.2-final/validation-receipt.json)
- [Interim V8.2 migration and provenance](evaluation/migration-v8.2/REPORT.md)
- [V8.2 migration ledger](evaluation/migration-v8.2/migration-ledger.json)
- [Canonical state](evaluation/evaluation-state.json)
- [Correction and migration report](evaluation/migration-v8.1/CORRECTION.md)
- [Detailed correction ledger](evaluation/migration-v8.1/correction-ledger.json)
- [Validation results](evaluation/migration-v8.1/correction-validation.json)
- [Evaluation result](evaluation/scoring-v82-final/evaluation-result.v12.json)
- [Web report](evaluation/scoring-v82-final/web-report.v10.json)
- [Canonical public projection](evaluation/scoring-v82-final/v8-canonical-projection/projection.v1.json)

| Dimension | V8.2 score |
| --- | ---: |
| Meaningful Coverage | 80.04% |
| Editorial Selectivity | 64.98% |
| Conceptual/Stance Fidelity | 97.63% |
| Page-reference Reliability | 89.34% |
| Findability/Navigation | 86.93% |
| Mechanics/Consistency | 100.00% |

The delivered entry “Senez, see of, 143” is now faithfully represented as a
heading and supported locator. All 6,221 original locator judgments are unchanged;
one targeted source check adds the recovered locator, giving 6,222 assignments.
All benchmark content and missing-access judgments are preserved. The targeted
structure review retains supplemental-route deductions and yellow signals while
removing their unsupported classification as destroyed access. Independent major
heading-fit findings remain.

The source has 425 mapped pages and 17 approved chunks. The frozen candidate-blind
benchmark release remains `98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab`; only its active
policy binding and content hash changed. No new discovery or independent review
was performed. Restricted source and candidate PDFs are excluded from Git.

## Validation and reporting

Run `python3 -m unittest discover -s tests -v` for historical projection and
current correction regression checks. The current runtime's registered `score`
and `build-report` commands produce the canonical outputs. Between those two
commands, `python3 scripts/project_v81_review_signals.py` projects the native
supplemental-route findings into score-free yellow report signals. The installed
runtime currently derives that particular signal only from structured defects.
This supplement changes no arithmetic, caps, gates, or audit judgments.

The current report supplies all six dimension denominators. Existing completed
outputs require explicit invalidation/replacement; do not run the historical
V8 builder against current V8.2 evidence. No website deployment has been made.

## Preserved history

The independent Senez repair and targeted V8.1 correction remain at
`48bb67b434335cd90002f7bf2078a8a176e2a525`, with their exact scoring/report bytes
under `evaluation/scoring-v81/`. The V8.2 migration reuses that 85.12% checkpoint.
It records actual candidate visibility and preserves the original candidate-blind
freeze separately. All six dimensions, numeric components, deductions and caps
are invariant; only version identities, evidence bindings and publication gates
change. No source discovery, normalization or substantive audits were rerun.


The original V8 evaluation scores **77.40%** and is preserved at
`11a3710435a4f870378929652cbc3f7c7e5f459b`. Its original scoring/report files remain
under `evaluation/scoring/`, and its public projection under
`web/v8-canonical-projection/`; these are historical, not the current output.
Use the complete original Git tree to reproduce its input hashes.

The [bounded migration review](evaluation/migration-v8.1/REPORT.md) and its
83.74% policy-only diagnostic are preserved as the earlier checkpoint, superseded
by the authorized correction documented above. Run
`python3 scripts/check_v81_migration_boundary.py` to verify that historical
review against its Git snapshots.

## Rights

Derived analytical artifacts may refer to headings and locators needed to explain
findings. Source and candidate PDFs must be obtained from authorized sources.

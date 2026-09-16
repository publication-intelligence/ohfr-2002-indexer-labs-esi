# Subject Index Evaluation: IndexerLabs / The Oxford History of the French Revolution (2002)

The current evaluation uses **V8.1** and scores **85.12%**, with valid evaluation
evidence, no triggered publication gates, and two non-binding 90% ceilings.
This result applies only to `subject-index-standard-policy-v8.1`,
`subject-index-rubric-v8.1`, and `subject-index-dimension-calculation-v6`.
A further methodology migration and website cutover are on hold pending the
coordinator's verified release/install receipt.

## Current artifacts

- [Canonical state](evaluation/evaluation-state.json)
- [Correction and migration report](evaluation/migration-v8.1/CORRECTION.md)
- [Detailed correction ledger](evaluation/migration-v8.1/correction-ledger.json)
- [Validation results](evaluation/migration-v8.1/correction-validation.json)
- [Evaluation result](evaluation/scoring-v81/evaluation-result.v12.json)
- [Web report](evaluation/scoring-v81/web-report.v10.json)
- [Canonical public projection](evaluation/scoring-v81/v8-canonical-projection/projection.v1.json)

| Dimension | V8.1 score |
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
V8 builder against current V8.1 evidence. No website deployment has been made.

## Preserved history

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

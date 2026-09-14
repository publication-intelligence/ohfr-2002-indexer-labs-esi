# Subject Index Evaluation: IndexerLabs / The Oxford History of the French Revolution (2002)

Candidate-specific evaluation artifacts for the IndexerLabs subject index to William Doyle's *The Oxford History of the French Revolution*, 2002 edition.

## Current V8 run

[`evaluation/evaluation-state.json`](evaluation/evaluation-state.json) is the only
canonical control file. All V8 stages are complete: candidate preparation,
locator auditing, missing-access auditing, global structure auditing, scoring,
and web-report generation.

The exact 425-page source identity, previously approved one-to-one page labels,
and previously approved 17 chapter boundaries were revalidated under the current
schemas. A fresh standard V8 policy was frozen before source discovery. The
restricted source PDF and derived chapter PDFs remain local and are excluded by
`.gitignore`; the registered page map, chunk manifest, policy, and chunk sidecars
live under [`evaluation/source/`](evaluation/source/).

The candidate-blind frozen benchmark was not rebuilt. It was imported from
[`publication-intelligence/ohfr-2002-esi-benchmark`](https://github.com/publication-intelligence/ohfr-2002-esi-benchmark)
at freeze `98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab` after exact source, page-map,
chunk, and benchmark-identity checks plus a separate V8 compatibility review.
The import provenance and approval are under [`evaluation/validation/`](evaluation/validation/).

[`completed-evaluation.portable.zip`](evaluation/checkpoints/completed-evaluation.portable.zip)
is the final portable recovery checkpoint. It contains 92 registered artifacts
and intentionally omits the 17 restricted source packet PDFs.

## Result

The independently reproduced V8 overall score is **77.43%**.

| Dimension | Score |
| --- | ---: |
| Meaningful Coverage | 80.04% |
| Editorial Selectivity | 65.17% |
| Conceptual/Stance Fidelity | 97.63% |
| Page-reference Reliability | 80.00% |
| Findability/Navigation | 60.00% |
| Mechanics/Consistency | 99.99% |

The locator audit covers 6,221 atomic assignments: 5,914 supported, 71 partially
supported, and 236 unsupported. Missing-access auditing covers 1,366 subjects,
1,026 reader tasks, and 3,210 treatments; 2,705 treatments were found and 505
were missed. The published score triggers the see-substitution, cross-reference,
and clutter gates. See [`evaluation-result.v12.json`](evaluation/scoring/evaluation-result.v12.json)
and [`web-report.v10.json`](evaluation/scoring/web-report.v10.json) for the exact
calculation and report projection.

Density remains provisional: chapter-level counts total 195,346 words, 628 words
(0.32%) above the imported legacy whole-book aggregate, and no registered
per-unit word-count artifact is available to resolve the difference.

## Contents

As the evaluation advances, this repository will contain:

- normalized candidate-index data;
- locator routing packets and exception ledgers;
- complete locator audits;
- missing-access and hierarchy audits;
- density and navigation analysis;
- scores and report-ready JSON.

It excludes source PDFs, chapter packet PDFs, extracted source text, and candidate PDF files.

## Candidate conversion

The supplied candidate is
`/home/john/Downloads/IndexerLabs_Oxford.pdf` with SHA-256
`7ab2d4d6db349973730e44f40b54365046d205be12c39d54e6dd5f1d9d595af1`.
The standalone evaluator utility converts it to
[`candidate-layout-extraction.v1.json`](candidates/oxford-history-french-revolution-2002-indexerlabs-truncated/candidate-layout-extraction.v1.json).

The converter's repeated-furniture fix now reproduces the checked-in layout
artifact byte-for-byte: 2,211 extracted lines, 49 excluded running-header lines,
and 2,162 retained index lines. Mechanical normalization has also produced the
registered candidate-index V2 and item-inventory V2 artifacts under
[`evaluation/candidates/`](evaluation/candidates/), with 1,644 normalized paths,
5,055 displayed locators, and 6,221 atomic assignments. Normalization completed
with no unresolved issues or locator-routing exceptions.

## Next stage

No evaluation stage remains. Use the final checkpoint for resume or transfer,
and regenerate deterministic scoring/report artifacts only after an approved
change to a registered input.

## Rights

Derived analytical artifacts may refer to headings and locators needed to explain audit findings. Source and candidate PDFs must be obtained separately from their authorized sources.

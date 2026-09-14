# Subject Index Evaluation: IndexerLabs / The Oxford History of the French Revolution (2002)

Candidate-specific evaluation artifacts for the IndexerLabs subject index to William Doyle's *The Oxford History of the French Revolution*, 2002 edition.

## Current V8 run

[`evaluation/evaluation-state.json`](evaluation/evaluation-state.json) is the only
canonical control file. It was initialized with the current V8 workflow from
`evaluate-subject-index` commit `66b63bc` and currently stops at
`source_subject_discovery`.

The exact 425-page source identity, previously approved one-to-one page labels,
and previously approved 17 chapter boundaries were revalidated under the current
schemas. A fresh standard V8 policy was frozen before source discovery. The
restricted source PDF and derived chapter PDFs remain local and are excluded by
`.gitignore`; the registered page map, chunk manifest, policy, and chunk sidecars
live under [`evaluation/source/`](evaluation/source/).

[`source-preparation.portable.zip`](evaluation/checkpoints/source-preparation.portable.zip)
is the portable recovery checkpoint for this milestone. It intentionally omits
the 17 restricted source packet PDFs.

The former `benchmark.lock.json` described an obsolete policy/rubric contract and
has been removed. Do not migrate or reinterpret that historical benchmark as a
current V8 benchmark. Source discovery, synthesis, independent review, and freeze
must produce current-schema artifacts in this canonical state.

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
current candidate-index V2 and item-inventory V2 drafts under
[`evaluation/candidates/`](evaluation/candidates/). The 25-item normalization
issues ledger under [`evaluation/validation/`](evaluation/validation/) still
requires explicit review and disposition, so candidate preparation is not yet
registered in canonical state.

Source discovery must happen in candidate-blind contexts; do not expose the
candidate layout or this repository's candidate directory to discovery workers.

## Next stage

Run candidate-blind source discovery for all 17 registered chunks, validate the
complete batch, synthesize and independently review the benchmark, and freeze it
with the typed V8 transition. Candidate normalization may proceed mechanically in
a separate context, but registration waits for benchmark freeze.

## Rights

Derived analytical artifacts may refer to headings and locators needed to explain audit findings. Source and candidate PDFs must be obtained separately from their authorized sources.

# Final V8.2 migration with scoped uncertainty

The final canonical score is **85.12%**, exactly matching the corrected V8.1
checkpoint `48bb67b434335cd90002f7bf2078a8a176e2a525`. All six numeric dimensions,
components, deductions, denominators, triggered/binding ceilings, diagnostic
grades and overall rounding are invariant. The two triggered 90% ceilings remain
non-binding. Evaluation validity is valid.

Publication readiness is **not_publication_ready**. The finalized evidence
triggers `GATE-WRONG-LOCATOR` for 140 distinct unsupported/no-fit locators and
`GATE-BROKEN-REFERENCE` for two absent supplementary reference destinations.
These are 142 distinct delivered items, not 142 separate gate rules. The reference
IDs are `XREF-1FB84F43D7ED` and `XREF-80B3F994D3ED`. Partial/nonzero fits do not
qualify for the direct wrong-locator gate.

Gate assessment remains **indeterminate** for 970 explicitly identified uncertain
locators. Eleven frozen uncertainty statements enumerate medium-confidence audit
rows. Their evidence IDs exactly match those rows; their accompanying path IDs
supply heading context. Each added `locator_support` scope therefore names only
its enumerated locators. No uncertainty was resolved, deleted, or narrowed in the
original record. All original uncertainty objects and all audit judgments remain
unchanged. No benchmark-access or whole-path uncertainty scope was inferred from
a kind string. The prepared evidence review is preserved in
`../migration-v8.2-patch-preparation/uncertainty-scopes.draft.json` (the filename
records its preparation status; the exact scopes are now applied).

The interim `adeb691` checkpoint is preserved at
`5a518e81dedef24f071018fe8b91f8bf5235d540`, with its original outputs in
`scoring-v82/` and a verified private recovery archive. That runtime incorrectly
expanded path uncertainty to sibling locators. Reviewed methodology PR50, merged
as `c11c6ccb16000fe79646af16b7be01f6cbeeac78`, corrects that behavior. Its 111-file
installed receipt has SHA-256
`f7d0b2bd830dfbca7b1e8c4f79c6320e2c7a945d075342807d24d6f9f7cd1204`.
The gate change from 87 to 140 confirmed wrong locators is a runtime consequence
of properly scoped evidence, not a new source audit or changed judgment.

Native retrospective policy provenance remains unchanged: actual migration
candidate visibility is true; the original candidate-blind policy/freeze,
review, compatibility approval and release evidence remain separate preserved
records. The independent Senez repair remains the V8.1 baseline. No discovery,
normalization, benchmark review, locator audit or missing-access audit was rerun.
The policy/rubric remain V8.2 and calculation profile v7. Only the structure
supplement, necessary registered hashes and derived outputs change in this patch.

The registered structure, score and report commands built `scoring-v82-final/`.
The existing score-free supplemental-route helper preserves the 70 yellow review
signals without altering arithmetic or gates. Validation and the final ledger
record exact output hashes and numeric invariance. Private checkpoints preserve
all registered inputs and restore cleanly; private recovery archives include the
prior original/repair/interim histories, exact runtime and validation logs.

This work creates reviewable evaluation artifacts. It does not merge the evaluation
PR or deploy the website. Assessment gaps remain disclosed alongside the confirmed
quality gates.

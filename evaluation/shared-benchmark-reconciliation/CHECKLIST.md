# Shared-benchmark reconciliation preparation

Status: inspection only. No policy, benchmark, audit, canonical state, score or
public bundle was changed. No activation, push, merge or deployment is authorized
by this preparation. PR #5 remains draft under the comparison hold.

## Verified baseline

The authoritative legacy v3 release is
`98dbffd0ca171b5b7db76dbe1b2b5d5265ccacab`. The exact frozen benchmark file and
canonical self-hash match the coordinator's lock. The local imported legacy file
also matches the frozen Git blob byte-for-byte.

The current import is exactly equal after only the approved
`relationships[*].type` to `relationship_type` normalization and exclusion of
six wrapper fields: benchmark ID, version, policy binding, freeze wrapper,
benchmark self-hash, and compatibility-import record. Every other field is equal,
including subjects, evidence, reader tasks, relationships, exclusions,
uncertainties, source/page-map/chunk identities, blindness, and substantive review
and synthesis provenance. Counts are 1,366 subjects, 1,026 tasks and 3,460
relationships; the existing audit treatment population is 3,210.

All 17 density word counts match the discovery Git blobs at that same release,
totaling **194,718 indexable source words**. These are already the locked legacy
source-discovery basis, not a substitute denominator inferred from subject count.
The policy uses word-weighted chapter density. Candidate path/locator counts
remain those of the separately preserved Senez correction. The policy density
metric provenance labels say V8.1 while the structure's copied labels say V8;
numeric bands and weights agree. A future basis identifier should distinguish
measurement provenance from policy calibration, without inventing new counts.

The final private archive, checkpoint and all 125 staged registered artifact
hashes were reverified unchanged. Remote refresh shows main still at `b9c2fa4`.
The final evaluation baseline remains `b55b79d`, 85.12%; this is not a statement
of cross-candidate comparability.

## Minimum changes when methodology support lands

1. Verify the installed release receipt and read the typed study-lock and density
   basis contracts. The inspected installed runtime has neither field, so do not
   invent JSON keys or an unofficial scoring wrapper now.
2. Attach the explicit study identity to the same legacy-v3 content using the
   native migration command. Reuse original review/compatibility approval and
   release evidence. Preserve the original August 24 freeze separately from the
   historical September 14 import wrapper. The legacy freeze contains its
   historical systemic-defect merge-block annotation; preserve it with the later
   release/compatibility evidence rather than silently rewriting that history.
   Keep retrospective `candidate_seen: true`; claim no fresh independent review.
3. Bind the 17 verified discovery-file hashes and source word counts through the
   supported density-basis contract. No new extraction/counting or density
   recalibration is justified by this inspection. If the study chooses different
   bands or a different measured basis, stop and document the explicit change;
   do not force the old score to survive a substantive method change.
4. Rebind only dependent wrapper hashes and the candidate-to-benchmark binding.
   Rebuild/register locator packets if required by the new wrapper identity.
   Preserve every semantic payload and stable ID.
5. Register unchanged/rebound audits through supported commands as required;
   register structure only for typed basis/provenance additions. Rebuild score,
   report and all public collections. Validate semantic identity and every
   component/cap/diagnostic against the final baseline. Numeric invariance is
   expected only if settings and counts remain identical.
6. Check shared study identity, source, page map, chunks, policy, audit mode,
   rubric, calculation profile and density basis across the study before making
   directly comparable-score claims. Matching subject counts alone is inadequate.
7. Preserve new private checkpoint/runtime and verify restore and saved-project
   handoff. Keep the old private archives immutable. Await explicit authorization
   for activation, publishing, merge and deployment.

## Artifact reuse matrix

| Artifact family | What remains valid | Minimal future action |
| --- | --- | --- |
| Source, page map, chunks, legacy discovery/review | Exact identities unchanged and bound to locked release | Reuse; attach study provenance |
| Normalized candidate, layout, inventory | Candidate-only; final Senez repair preserved | Reuse bytes; update state benchmark binding only |
| Benchmark semantic payload | Exact normalized identity with locked v3 | Native wrapper/study-lock migration only |
| 17 locator audits / 6,222 judgments | Source/candidate evidence unchanged | Reuse judgments and bytes unless contract requires binding fields |
| 17 missing-access audits | Same subjects, tasks, treatments, priorities and routes | Reuse every judgment; rebind benchmark hash if changed |
| 17 locator packets | Same candidate routing and benchmark payload | Mechanical regeneration/rebinding if wrapper hash changes |
| Structure findings, reference resolutions, uncertainty scopes | Same stable populations and evidence | Preserve findings; add supported density-basis provenance only |
| Density measurements | All 17 word counts verified at locked release | Reuse numbers; type their basis without guessing schema |
| Calculation/result/report/projection | Historical baseline, not reusable as newly bound output bytes | Rebuild after native rebinding and prove numeric invariance |
| Original approvals/freezes/private archives | Historical provenance | Preserve unchanged; no new approval or blind review claim |

## Executed read-only check

Run `python3 scripts/check_shared_benchmark_lock.py --benchmark-repository PATH`
against the repository containing the locked commit. It verifies exact frozen
bytes/self-hash, complete normalized semantic equality, all 17 discovery count
bindings and all currently registered artifact hashes. `inspection.json` records
its public-safe result. This receipt is preparatory documentation, not a second
canonical state or a native study lock.

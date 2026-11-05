# Whole-Paper Review Checklist

## Pass 1: Argument and coverage

Record the exact current files and task scope first. An instruction to inspect is not permission to rewrite; an instruction to fix only two tables does not permit resetting image sizes or editing the abstract.

- Every requested deliverable maps to a section and final result.
- Question dependencies are explicit and correctly ordered.
- Problem analysis, detailed model, result interpretation, and abstract serve different roles.
- Each major subsection completes the process chain.
- Method choice follows problem/data structure.
- Assumptions are specific, used, and tested when testable.
- Results answer the question rather than only report software output.
- Validation supports the exact claim made.

Report high-impact mathematical/logic defects before style or formatting issues.

## Pass 2: Consistency matrix

Build a table for decisive claims:

| Claim/result | Abstract | Body | Figure/table | Conclusion | Appendix/code | Status |
|---|---|---|---|---|---|---|

Check:

- numbers, signs, percentages, denominators, ranges, precision, and units;
- sample count versus record count;
- symbol definition, first use, vector/scalar form, and subscript;
- equation numbering and every cross-reference;
- figure/table numbering, caption, introduction, and interpretation;
- question and section numbering;
- model name and solver name are not confused;
- conclusion does not add a new unsupported claim.

Use `scripts/audit_text.py` on text exports for surface leads, then verify semantically.

## Evidence and citations

- Every external factual claim or borrowed relation has a credible source where needed.
- Citation numbers/names resolve to reference entries.
- References are actually cited.
- No fabricated source, DOI, result, or test appears.
- AI-use disclosure follows current competition rules.

## Reproducibility

- Run the original workflow without edits and preserve its command/output before repairing a conflict.
- Code corresponds to the described method and units.
- Seeds, solver settings, bounds, stopping criteria, and data paths are sufficiently described.
- Decisive outputs can be traced through formula, code, intermediate output, and canonical result artifact.
- Related figure/table exports are regenerated from that artifact rather than typed independently.
- Confirmed code defects have a minimal failing test plus repaired and regression-test evidence.
- Appendix code is grouped by question and is readable/executable where required.
- The body contains enough evidence without requiring judges to run all code.

For conflicts or suspicious outputs, load [model-code-debugging.md](model-code-debugging.md). For complete provenance, load [evidence-traceability.md](evidence-traceability.md).

## Rendered-page QA

Check grouped equations against [equations-word.md](equations-word.md): one semantic group, one left brace, internal left alignment, one number, no clipped last row. A text search for a new path or formula fragment is not a full statement/syntax check.

Render PDF/DOCX and inspect every page or a contact sheet plus flagged pages:

- clipped formulas, missing glyphs, black boxes, or low-resolution plots;
- tables crossing margins or unreadably small text;
- detached captions and figures/tables appearing before introduction;
- inconsistent heading hierarchy, fonts, spacing, and indentation;
- excessive blank pages/space and bad page breaks;
- headers, footers, page numbering, reference and appendix transitions;
- color-dependent information that becomes ambiguous in grayscale.

Visual polish never compensates for an incomplete argument, but layout defects can hide correct work.

Load [figure-table-workflow.md](figure-table-workflow.md) for figure/table selection, numerical reconciliation, final-size QA, and automatic regeneration rules.

## Review output labels

State which checks were static, visual at full size, unit-test, short-run or full recomputation. Report precise open issues; do not equate a contact sheet with every formula verified. Do not predict award probabilities or claim a rank from apparent polish.

Use these labels so the author knows what to do:

- **Must fix:** mathematical contradiction, missing answer, fabrication risk, unit/value conflict, invalid assumption, leakage, or non-reproducible core step.
- **Should fix:** weak interpretation, incomplete validation, unclear dependency, or unsupported adjective.
- **Polish:** wording, typography, spacing, or minor ordering.
- **Cannot verify:** missing data, code, result file, or unreadable source.

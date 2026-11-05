# Evidence Traceability and Reproducibility

Build one ledger for decisive claims:

`problem statement -> formula/model -> code location -> intermediate output -> canonical result artifact -> figure/table -> body -> abstract/conclusion`

## Coverage ledger

| Requirement | Section | Formula/model | Code location | Input/source | Intermediate output | Final result | Figure/table | Validation | Abstract/conclusion |
|---|---|---|---|---|---|---|---|---|---|

Every requested deliverable needs one complete row. A missing row is a coverage defect even when the prose is fluent.

## Canonical artifact rule

Store decisive unrounded results in one canonical result artifact such as CSV, XLSX, JSON, Parquet, or a documented program object. Generate manuscript tables, figures, and repeated body values from it. Do not type independent copies into each surface.

Record:

- source file, sheet/table, fields, join keys, filters, and row counts;
- transformations, units, coordinate convention, ordering, and precision rule;
- script/function and command that generate each result;
- environment, dependency versions, random seed, solver settings, and stopping rule;
- output file paths and timestamps or hashes where useful.

## Symbol and unit registry

For every important symbol record meaning, domain, unit, coordinate frame, sign convention, formula location, code name, and figure/table label. Resolve conflicts before polishing prose.

## Citation and assumption provenance

Classify each premise as:

- given by the problem;
- measured or derived from supplied data;
- author assumption;
- standard relation requiring no special attribution;
- externally sourced fact, parameter, formula, or method requiring citation.

For each citation record the exact claim it supports. A bibliography entry without claim-level support is not evidence.

## Change propagation

When a model or code repair changes a result:

1. regenerate the canonical artifact;
2. diff key values, units, precision, and feasibility status;
3. regenerate affected figure/table outputs;
4. update body interpretations and cross-references;
5. update abstract/conclusion only after body results are stable;
6. rerender the final paper and verify all affected pages.

Do not synchronize ambiguous mappings automatically. Report candidate destinations and request a mathematical choice.

## Results, tests and appendix are separate surfaces

Tests calling a real `main()` with mocked states must redirect **all** output writers to temporary directories. Mocking `write_resultN()` alone is insufficient if `main()` also writes a JSON summary. Check that output artifacts are unchanged after tests.

A diagnostic JSON containing zero states and unit properties is not a valid numerical record merely because unit tests pass. Regenerate it from a trustworthy run or remove it if it is not a required deliverable; do not reconstruct unrounded extrema or iteration counts from rounded Excel values.

After reorganizing directories, update input paths, output constants, imports, test loaders, plotting inputs, README/run commands, audit links and printed appendix code together. Generate code listings from the canonical source files. Check complete statements and syntax; searching for an obsolete path's absence misses a dangling operator such as `OUT = Path(__file__).parent /`.


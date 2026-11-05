# Model-Code Joint Debugging

Use this workflow when code, data, computed results, figures, tables, or manuscript claims may be wrong.

## Required discipline

For conflicting results, reproduce the symptom and trace its root cause before patching. Add a meaningful regression check when it can distinguish the defect from correct behavior, then run fresh verification before claiming completion.

If installed, `superpowers:systematic-debugging`, `superpowers:test-driven-development` and `superpowers:verification-before-completion` can help apply this discipline. They are optional integrations; follow the complete workflow below when they are unavailable. Do not ask users to install unrelated skills just to use this package.

Reproduce before editing. Do not patch a suspicious line merely because it looks unusual.

## Verification chain

Trace the earliest divergence across:

`problem statement -> formula/model -> code -> intermediate output -> final result -> figure/table -> paper`

Classify every finding as one of:

- `problem-interpretation`
- `mathematical-model`
- `data`
- `implementation`
- `numerical-method`
- `paper-reporting`
- `cannot-verify`

## Phase 1: Reproduce

1. Inventory inputs, runtime, dependency versions, command, random seed, expected output, and generated files.
2. Run the original workflow without changes and preserve the command and output.
3. Locate the earliest incorrect intermediate value, not only the wrong final answer.
4. Trace it backward across function, data, unit, and model boundaries.

If reproduction is impossible, identify the missing artifact or environmental difference. Do not guess a repair.

## Phase 2: Establish an independent oracle

Compare the affected route with at least one applicable oracle:

- hand calculation or analytic special case;
- dimensional, boundary, symmetry, conservation, or limiting-case check;
- tiny brute-force optimization instance or independent solver;
- raw-prediction metric recomputation;
- group/time-aware leakage check;
- grid, time-step, tolerance, initialization, or multi-seed stability check.

Build a traceability row:

| Paper element | Formula/rule | Code symbol/function | Input | Intermediate output | Test |
|---|---|---|---|---|---|

## Phase 3: Confirm one root cause

State one falsifiable hypothesis:

`The root cause is X because evidence Y predicts observable Z.`

Create a minimal failing test for Z and run it. A failed hypothesis returns to evidence gathering. Do not stack speculative changes.

Stop rather than choose silently when two mathematical interpretations remain defensible.

## Phase 4: Repair and retest

After the minimal test confirms the root cause:

1. Automatically repair the smallest responsible code or structured source.
2. Rerun the minimal failing test.
3. Rerun the original reproduction command.
4. Run neighboring-question and whole-pipeline regression checks.
5. Recompute objectives, constraints, metrics, and decisive values independently.
6. Regenerate affected figures and tables from the canonical result artifact.
7. Synchronize captions, body, abstract, conclusion, and attachments when mappings are unambiguous.
8. Preserve unrelated user changes and the original result artifacts.

After three failed repair attempts, stop, reassess the model or decomposition, and gather new evidence.

## Type-specific checks

### Physical, geometric, simulation, inverse

- units and coordinate conventions;
- initial/boundary/interface conditions;
- conservation, monotonicity, and analytic cases;
- discretization and solver convergence;
- forward/inverse consistency.

### Optimization and scheduling

- bounds, domains, indices, time references, and resource conservation;
- direct constraint and slack recomputation;
- objective recomputation outside the optimizer;
- tiny-instance enumeration or independent solver;
- repeated seeds without confusing repeatability with global optimality.

### Statistics and prediction

- row, participant, and sample counts after every transformation;
- join keys, label order, missingness, duplicate handling, and leakage;
- preprocessing fitted only inside training folds;
- metric, uncertainty, threshold, and confusion-matrix recomputation;
- fixed-seed reproducibility and multi-seed stability when relevant.

## Repair report

For every confirmed repair report: symptom, root cause, evidence, changed file/function/formula, failing-test result, regression evidence, old/new result, unit/precision, and affected paper sections or artifacts.

## Specific failure patterns from the drying case

- **Initial layer:** uniform initial state can conflict with an immediate Robin flux. Good final-time convergence says nothing about the first seconds. Compare the complete output grid and the worst boundary-time location; use a justified damped startup where needed, not a different physical PDE merely to suppress an artifact.
- **Boundary source:** a program can include the old/new ambient source while the manuscript CN equation omits it. Check capacity normalization and the entire source vector before declaring the equation wrong.
- **Precision:** a difference below half a displayed unit does not by itself prove both values round identically near a rounding boundary. Compare the displayed outputs directly and bound the relevant error.
- **Conservation:** absolute residuals carry units and geometry normalization; publish both those units and a clearly defined scale for a normalized residual. Handle a zero exchange scale explicitly.
- **Strict threshold:** retain the unrounded inequality, crossing bracket, interpolation time, extrapolated time, first discrete passing step and first saved row. Displayed `0.1500` can represent a value below or above `0.15`.
- **Test contamination:** running a mocked main must not change production JSON/XLSX. Capture artifact hashes before and after tests or isolate every writer.
- **Relocation:** files moved into folders can break main inputs, test loading, audit imports and figure sources independently. Test from the extracted final package, using the documented commands.


# Award-Case Structural Patterns

These notes paraphrase structural observations from five official national-award paper pages. They are not prose templates and do not certify every choice in a paper.

## 2024 A242: geometric motion and optimization

- The abstract gives a method and an exact answer for each question.
- Questions form a chain: motion state, collision detection, pitch optimization, turn path, then speed optimization.
- Main sections repeatedly use establish, solve, and validate.
- A validation/analysis result in one question narrows the next search interval.

Transferable lesson: expose recursive dependencies and show how intermediate findings reduce the next problem.

## 2025 A196: mechanism and layered optimization

- A question-relationship diagram shows progression from fixed parameters to single/multiple projectile and agent cases.
- The paper proves simplifying geometric claims before searching.
- When the full decision space is too large, it explains the dimensional difficulty and separates task allocation from parameter optimization.

Transferable lesson: justify decomposition and state each layer's contract. Do not merely announce a heuristic algorithm.

## 2025 C132: heterogeneous longitudinal data

- Repeated measurements motivate a mixed-effects model and participant-level variation is quantified.
- Model conditions and comparisons are tested rather than only asserted.
- Later questions move from a single-factor grouping decision to multivariate time-dependent prediction and classification.

Transferable lesson: method choice follows observation structure, and model output feeds a decision model.

## 2025 B060: physical inverse problem

- A physical forward model precedes two inversion routes.
- Direct period calculation and iterative curve inversion cross-check thickness estimates.
- A criterion is derived for whether multi-beam effects matter; correction is applied and compared with the base result.

Transferable lesson: combine derivation, independent verification, applicability conditions, and correction.

## 2025 C023: statistical decision framework and counterexample

- Questions are organized as separate model-and-solution chapters with sensitivity or validation.
- The paper combines repeated-measure modeling with grouped timing decisions and a separate abnormality procedure.
- It also includes assumptions such as attachment-data accuracy and residual normality without first presenting the required checks in the assumption wording.

Transferable lesson: award status is not evidence that every assumption, title, or sentence should be copied. Apply source priority and mathematical diagnostics.

## Cross-case pattern

Strong reusable structure is:

```text
question property -> model choice -> derivation or construction
-> intermediate result -> contextual interpretation
-> next question/decision -> exact result -> validation
```

The cases differ in title style, assumption quality, model complexity, and validation strength. Preserve the structure that improves traceability, not surface imitation.

## Page-level reasoning and evidence index

Use these observations as retrieval cues. Page numbers refer to the inspected official award-paper PDFs; paraphrase the pattern and never reproduce the original wording or artwork.

| Case/page | Evidence sequence | Transferable use | Do not copy |
|---|---|---|---|
| 2024 A242 p.6 | polar/state definition -> neighboring geometry diagram -> cosine relation -> recurrence -> Cartesian conversion | linked geometry, motion, collision, and recursive state models | original object, notation, distances, or diagram |
| 2024 A242 p.12 | search goal -> two-stage flowchart -> numbered coarse/fine search -> exact terminal values | event-time location and precision-controlled search | decorative dashed containers or unverified precision |
| 2024 A242 p.16 | solver-choice rationale -> PSO flow -> parameter disclosure -> objective curve plus convergence -> constraint interpretation | heuristic optimization with separate behavior and convergence evidence | claim that convergence proves global optimality |
| 2024 A242 p.19 | path geometry diagram -> tangent relation -> parameter derivation | geometry-to-parameter derivation | source-specific path labels and values |
| 2024 A242 p.25 | representative exact-value table -> fixed-scale time snapshots | dynamic solution reporting | inconsistent axes or redundant full-state tables |
| 2025 A196 p.3 | question-dependency diagram -> separate analyses with inherited decisions | multi-question dependency planning | visual decoration without explicit contracts |
| 2025 A196 pp.8,13 | line-of-sight schematic -> algebra; 3-D object simplified through a proved cross-section relation | mechanism simplification before search | treating an intuitive sketch as proof |
| 2025 A196 p.15 | algorithm flowchart -> matching numbered steps and stopping rules | reproducible algorithm exposition | mismatched node and prose terminology |
| 2025 C132 pp.10,13-14 | relationship exploration -> model choice -> Q-Q/residual diagnostics -> assumption decision | statistical model selection and diagnosis | unreadably dense panels or visual-only conclusions |
| 2025 C132 p.24 | exact recommendation table -> confidence-response curves -> clinical/decision interpretation | policy values plus sensitivity to confidence requirements | repeating all curve points in the table |
| 2025 C132 pp.29,34,38 | formula-defined architecture -> network diagram; importance plot -> mechanism discussion; threshold rule -> confusion matrix | prediction architecture, interpretation, and system validation | tiny labels, unexplained importance definitions, or reversed class order |
| 2025 B060 pp.14,24 | observed/fitted comparison -> optimizer convergence -> interpretation; base/corrected fit comparison -> loss convergence | inverse-model validation and correction | default plot labels or convergence-only truth claims |
| 2025 B060 pp.22,28 | suspicious points and physical threshold overlaid -> error propagation explanation | showing why an observation is unreliable | dual axes without semantic need or label-color matching |
| 2025 C023 pp.5-6 | preprocessing/model/solution/result flow -> descriptive table -> relationship heatmap -> model formula | data-to-model process chain | decorative infographic density or unreadable heatmap values |
| 2025 C023 pp.9,13 | test-summary table -> response curves; continuous risk curve -> discrete recommendation | exact evidence plus explanatory pattern | unsupported causal wording or unexplained confidence bands |
| 2025 C023 pp.21-22 | class counts -> subgroup distribution -> threshold scatterplots -> error interpretation | classification result, threshold, and subgroup stability | aggregate accuracy without error analysis |

## Retrieval rule

Select a pattern using:

`current missing link + subproblem property + evidence available + downstream decision`

Do not select by visual resemblance alone. After retrieval, apply the precondition and originality checks in [award-pattern-imitation.md](award-pattern-imitation.md).

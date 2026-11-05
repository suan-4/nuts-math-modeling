# Common Writing Rules

## Source priority

Use this order when guidance conflicts:

1. Current official problem, rules, and supplied data.
2. Mathematical/statistical validity and reproducibility.
3. Teacher writing principles.
4. Award papers as structural observations, never as unquestionable authority.

Do not copy source prose. Extract the decision rule behind it.

## Paper logic

The reader should be able to answer five questions at every stage:

1. What is being solved now?
2. Why is this operation needed?
3. What evidence or quantity enters it?
4. What comes out, and what does that output mean?
5. How does it affect the next operation or conclusion?

Writing, modeling, and coding should be developed together. Record derivations, parameter choices, intermediate tables, and validation while they are produced.

## Formatting authority and local preferences

Use the current competition rules and the user's designated template. The verified configuration for this project's 13-page template is in [template-profile.md](template-profile.md), including its internal heading-alignment conflict. Do not hardcode one user's local path or typography as a universal requirement.

Record template rules separately from later project preferences. Preserve locked manual image sizes, abstracts and local edits. For this project's code listing the template says Times New Roman **小五9pt**, not 五号10.5pt. Formula paragraphs may need local spacing exceptions; consult [equations-word.md](equations-word.md).

## Section roles

### Problem background and restatement

- Keep background brief and specific to the decision or mechanism.
- Restate deliverables, conditions, and outputs in the author's own language.
- Do not use background to inflate length or introduce unsupported facts.

### Problem analysis

This is the route from question to model. It should identify obstacles, decomposition, dependencies, and why the proposed mathematical object addresses the question.

Do not:

- copy the abstract and its final numbers;
- repeat detailed formulas from the model section;
- list model names without explaining their role.

### Assumptions

A useful assumption either comes from the problem or makes a necessary, defensible simplification. For each assumption ask:

- What complexity does it remove?
- Where is it used in the model?
- Would the current model fail if it were false?
- Can it be checked instead of assumed?

Do not assume attachment data are correct, residuals are normal, variance is constant, observations are independent, or a relation is linear when those properties are part of the analysis. Delete unrelated force-majeure boilerplate. Keep the list short and problem-specific.

### Symbols

- Include problem attributes, model inputs, decision variables, and newly defined indicators.
- Omit disposable local algebra symbols unless essential for reading.
- Explain each symbol again at first use in the body.
- Keep notation, subscripts, superscripts, vectors, units, and domains consistent.

### Model and results

- Keep heading depth to about three levels; use numbered steps below that.
- Give established algorithms only the explanation needed to understand their role and settings.
- Put results close to the step that produces them.
- Introduce every figure/table before it appears and interpret it afterward.
- Separate model definition, solution procedure, computed result, and validation.
- Deliver the requested answer/table/file before extended validation. Explain a change in assumptions before reusing a previous question's final state.
- Add a useful chapter lead-in that names the task and the coming model/output. Under intermediate headings, move an existing shared introduction rather than repeat it at every level.

### Evaluation and limitations

Use evidence: convergence, sensitivity, uncertainty, residual diagnosis, holdout performance, independent route, limiting case, or benchmark. A limitation must describe a real scope boundary or unmodeled mechanism, not generic self-criticism.

### Citations and appendices

- Cite domain facts, borrowed equations, and nontrivial methods where appropriate.
- Prefer primary, academic, official, or government sources over blogs.
- Ensure every reference is cited and every citation resolves.
- Appendices should make computations reproducible: executable code by question, full result files, and oversized tables/figures. The body must still contain the decisive evidence.

## Integrity language

Replace unsupported adjectives with measured statements:

- Not “precision is high”; report the error, convergence change, or benchmark difference.
- Not “robustness is strong”; report which inputs/scenarios were perturbed and how output changed.
- Not “significant”; report the test, estimate, uncertainty, and threshold.
- Not “optimal”; state the objective, feasible set, solver evidence, and whether global optimality is proved or only numerically supported.

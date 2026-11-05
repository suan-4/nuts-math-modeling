# Abstract and Title

## Title

Check official rules first. When self-titling is allowed, prefer the literal problem topic plus `研究`, `建模`, `分析`, `设计`, or another accurate action. Avoid `基于XX算法` when the paper uses multiple methods or the named algorithm is merely a solver.

A method-led title is justified only when one genuinely distinctive method organizes the whole paper. Award-paper usage does not override fit or official rules.

## Build an abstract matrix first

| Question | Method and why | Decisive intermediate step | Exact requested result | Validation/meaning |
|---|---|---|---|---|

Do not draft until every supported cell is filled. Put missing evidence in a separate gap list; do not invent a polished result.

## Paragraph contract

Each question paragraph must contain:

1. **Problem:** the quantity, decision, relation, or classification requested.
2. **Method:** the mathematical model and decisive operation, not every library/model tried.
3. **Result:** exact requested value, range, rule, category, or finding with unit and scope.
4. **Validation/meaning:** include when decisive and supported.

Use `problem -> method -> result`, not `problem -> list of methods -> stop`.

## Selection and precision

- Keep only final requested results and essential validation; omit most intermediate numbers.
- Preserve meaningful precision from the authoritative result table/code. Do not truncate incorrectly.
- Use the same unit, sign convention, sample definition, and denominator as the body.
- A rounded abstract value must be a correct rounding of the body value.
- Report a solver setting only if it explains validity or reproducibility.

## Evidence language

- Grid/point-count change supports numerical stability.
- Repeated solver runs support repeatability under current settings.
- Holdout metrics support predictive performance on the defined test population.
- Sensitivity analysis supports stability only over the tested perturbation range.
- An alternative model/route may support cross-validation if it is genuinely independent.

Do not inflate these into general accuracy, robustness, or superiority claims.

## Structure

A concise abstract may use:

1. One opening paragraph: context, overall task, and unifying approach.
2. One paragraph per question.
3. Optional closing sentence: defensible contribution, limitation, or applicability.
4. Four to five keywords drawn from topic, core model family, and major decision object.

Bold only the most important model, exact answer, or decisive finding if formatting permits. Excessive bolding removes hierarchy.

## Required files and honest contribution

When the problem requires named result workbooks, include the exact filename in the corresponding question's abstract paragraph as well as in the body and supporting-material list. File names are deliverables, not a substitute for quantitative results; create room by removing repeated method language. Never change `result1.xlsx` to `results1.xlsx` for stylistic consistency.

Open with a brief task-specific background conflict, then state the model and what was actually solved. Computing fields and endpoint times supports drying-pattern prediction, not an unperformed process optimization or measured energy saving. A short task phrase at each question's beginning can orient a reader who has not read the body.

Use “保留两位小数为57.47h” rather than “按百分位报告” when decimal rounding is intended. An extrapolated threshold, a discrete first-below time and a saved Excel row are different outputs; name them precisely.

## Final abstract audit

- Every question covered once and in correct order.
- No method without a result.
- No result absent from the body.
- No unit/precision conflict.
- No subjective adjectives without evidence.
- No result from a later question inserted into an earlier paragraph.
- Title represents the paper rather than advertising one solver.

# Data Analysis, Statistics, Prediction, and Classification

## Start from the analysis unit

Define:

- observational unit and number of independent units;
- repeated records, groups, batches, times, or spatial clusters;
- target, predictors, available-at-decision-time boundary, and evaluation unit;
- whether the task is description, association, prediction, causal inference, or decision support.

Do not confuse record count with participant/sample count.

## Question-specific preprocessing

For each question, report only preprocessing used by that question:

1. tables and fields selected;
2. joins/aggregation and resulting unit;
3. missingness and treatment;
4. duplicate and logical-consistency checks;
5. outlier definition, rationale, and sensitivity;
6. transformation/standardization and where parameters are learned;
7. resulting sample/feature counts.

Do not assume attachment data are correct. Do not delete extreme values automatically.

## Choose models from data structure

- Repeated measures: mixed-effects models, GEE, participant-level aggregation, or another justified correlation structure.
- Time-to-event or threshold time with censoring: survival framework.
- Time series: preserve temporal order and prevent future leakage.
- Imbalanced classification: stratified/group-aware evaluation and metrics beyond accuracy.
- Nonlinear/heterogeneous relation: justify flexibility from diagnostics or out-of-sample comparison.

A model name must be preceded by the property that makes it appropriate.

## Test rather than assume

Normality, equal variance, independence, linearity, stationarity, and proportional hazards are model conditions or diagnostics. State:

- what object is tested (raw outcome, conditional residual, random effect, etc.);
- diagnostic/test and result;
- consequence of violation;
- robust alternative used if necessary.

## Leakage-safe validation

- Split by independent unit, group, batch, or time as the data-generating process requires.
- Fit imputation, scaling, feature selection, resampling, and tuning inside training folds only.
- Keep a final test set untouched when sample size permits.
- Report uncertainty across folds/runs and the number of independent units.
- Match metrics to the question and class balance: MAE/RMSE, calibration, ROC-AUC, PR-AUC, recall, F1, decision cost, or another justified measure.

## Process-based result writing

Each subtask should immediately report and interpret its output:

```text
preprocessing output -> exploratory/diagnostic finding -> model choice
-> fitted/validated output -> contextual interpretation -> next model/decision input
```

Examples of explicit contracts:

- A correlation/feature screen determines the candidate variables for the next model.
- A fitted probability curve supplies risk values to a timing optimization.
- A clustering result defines groups whose profiles and stability must then be explained.

Never claim causation from observational association without an appropriate design and assumptions.

## Reporting

Apply [figure-table-workflow.md](figure-table-workflow.md) to distributions, correlation, diagnostics, response curves, thresholds, confusion matrices, subgroup errors, and compact statistical tables. Generate all displays from the same evaluated dataset and class order.

Include effect estimates/predictions, uncertainty, test-set or cross-validation results, confusion/calibration information where relevant, and sensitivity to preprocessing or error assumptions. Interpret practical magnitude, not only p-values.

# Process-Based Writing

## Three layers must differ

| Layer | It should answer | It should not become |
|---|---|---|
| Problem analysis | Why this route can solve the question | Abstract repetition or formula dump |
| Model establishment and solution | How the result can be reproduced | Algorithm-name list |
| Result analysis | What the output means and changes next | Table caption repetition |

## Process audit

For every substantive subsection, fill this ledger before rewriting:

| Link | Required content |
|---|---|
| Need | Current obstacle or quantity to determine |
| Input | Data, prior result, parameter, boundary condition, or assumption |
| Operation | Derivation, transformation, estimation, test, search, or solver step |
| Intermediate output | Quantity actually produced by the operation |
| Interpretation | Meaning in the original problem, not only mathematical meaning |
| Next decision | How the interpretation selects, constrains, or initializes the next step |
| Final result | Requested answer with value, unit, scope, or category |
| Validation | Independent check, sensitivity, uncertainty, convergence, or comparison |

Missing intermediate output or interpretation is the most common form of “only saying how the question was completed.”

## Diagnose before rewriting

Classify each sentence as one of:

- question/need;
- evidence/input;
- action;
- intermediate result;
- interpretation;
- transition/decision;
- final result;
- validation.

Then report the broken links. Do not hide a missing calculation by making the sentence more fluent.

## Repair with incomplete evidence

Use two separate blocks:

1. **Directly usable revision:** rewrite only facts already supported.
2. **Evidence to add:** list the exact table, value, parameter, rule, or test needed.

Avoid returning a polished paragraph dominated by bracketed blanks. If the method relationship is unknown, offer alternative structures explicitly instead of asserting one. Example: gray relational analysis might select features, set weights, or be an independent interpretation step; the manuscript/code must decide which.

## Minimal paragraph pattern

```text
To determine [quantity], use [specific input/prior output].
Because [problem property], perform [derivation/test/operation] rather than merely naming a method.
This produces [intermediate quantity].
The intermediate result shows [problem-context meaning], so [next choice/constraint].
Solving under these conditions gives [requested result and unit].
[Validation] supports only [precise claim], not a broader adjective.
```

## Dependency language

Prefer explicit contracts:

- “The collision threshold from Question 2 becomes the feasibility constraint in Question 3.”
- “The fitted probability curve supplies each group's risk at candidate times to the optimization model.”
- “The physical solver maps thickness vector to maximum temperature; the optimizer calls this mapping for every candidate.”

Avoid empty sequencing such as “first, then, finally” when no output is carried across the transitions.

## Transitions and result placement

A major question's modelling section should begin by stating its concrete task, inherited information, newly introduced condition, and what will be calculated below. One or two sentences normally suffice. A parent section needs a transition when it connects distinct subsections; it does not need a redundant introduction just because a heading follows. Prefer moving an existing shared first sentence upward.

For a requested result table, lead with the actual model and solver, the extracted time/position set and exact output filename. Then present the required table, explain its decisive values, and place plots and validation near that result. Do not lead with a long audit chapter before answering the original table-filling task.

“根据6.1—6.2模型建立和算法设计……” is a weak substitute for naming the radial diffusion model, finite-volume spatial discretization and nonlinear time stepping. Use only the specific methods that were actually implemented. See [chinese-writing-playbook.md](chinese-writing-playbook.md) for concise Chinese examples.

## Result interpretation prompts

- Why is this value plausible?
- Is it inside the permitted range?
- Which constraint is active?
- What physical/statistical/managerial mechanism explains the pattern?
- What later step uses it?
- What conclusion is not supported by it?

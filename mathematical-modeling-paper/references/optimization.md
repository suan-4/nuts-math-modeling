# Optimization, Decision, Scheduling, and Control

## Complete model definition

Every optimization model must expose:

1. Decision variables, domains, indices, and timing.
2. Parameters and which prior question supplies them.
3. Objective derived from the real goal.
4. Every constraint with its physical, logical, resource, policy, or statistical reason.
5. One consolidated mathematical program.

Do not call an algorithm the model. Genetic algorithms, particle swarm, simulated annealing, and differential evolution are solvers, not substitutes for variables/objective/constraints.

## Process chain

```text
real decision -> variables -> objective/constraints -> feasible candidate
-> solver evaluation -> best feasible solution -> constraint/meaning analysis
-> sensitivity or comparison
```

For sequential or layered problems, state why decomposition is necessary and what each layer passes to the next. Examples include task allocation before parameter optimization, prediction before scheduling, and physical simulation inside a design loop.

## Solver choice

Justify from model structure:

- continuity/discreteness;
- convexity or lack of proof;
- dimension and combinatorial size;
- differentiability;
- expensive simulation calls;
- multiple local optima;
- required precision and runtime.

Report initialization, bounds, stopping rule, population/iteration settings where relevant, and repeated-run behavior. Do not describe generic algorithm history.

## Result checks

- Verify all constraints numerically and report margins/slack.
- Identify active constraints and explain their real meaning.
- Report convergence or optimality evidence appropriate to the solver.
- Compare against a baseline, simplified case, alternative solver, or lower bound where possible.
- Run sensitivity on influential parameters and measurement error.
- Distinguish global optimum, proven optimum, best found solution, and local optimum.

Repeated identical runs support algorithmic repeatability under current settings; they do not alone prove model robustness or global optimality.

## Presentation

Apply [figure-table-workflow.md](figure-table-workflow.md) to convergence, sensitivity, Pareto/trade-off, schedule, and final decision outputs. Never use convergence appearance as the only feasibility or optimality evidence.

Include a compact decision table with variable values, objective value, units, and key constraint margins. If the answer is a schedule or allocation, show it in the form a decision maker can execute. Explain how the plan changes when a sensitive parameter changes.

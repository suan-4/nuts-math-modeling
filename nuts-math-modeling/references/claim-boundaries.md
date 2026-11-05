# Claim Boundaries for Modeling Papers

## Solution quality versus validity

Keep four claims separate:

| Evidence | Supports | Does not support alone |
|---|---|---|
| 独立验证 (independent validation) | constraint satisfaction and objective recomputation | global optimality or real-world accuracy |
| Solver status and MIP gap | reported bound gap under stated model/settings | theorem-level global optimality unless the solver proves it |
| Heuristic improvement history | improvement over its initial solution | global optimality or robustness |
| Sensitivity experiment | response under its stated perturbation protocol | untested re-optimization or causal generality |

With a time limit, nonzero MIP gap, or heuristic method, report a `current high-quality feasible solution` or `near-optimal solution`, together with solver status, bound, gap, stopping rule, and validation result. Use "global optimum（全局最优）" only when proof or certified solver completion supports it.

Never call materially different gaps "the same order" merely to blur their difference. Interpret the numerical magnitude and its decision relevance.

## Sensitivity and comparison

Label a fixed-decision experiment explicitly: `固定方案的后评估 (fixed-solution post-evaluation)`. If only auxiliary variables are re-optimized after holding the main decision fixed, say so. It does not compare the re-optimized strategies under each scenario and does not establish overall robustness.

For a comparison, list everything that differs: objective rule, decision variables, re-optimization, constraints, costs, data, and solver settings. Attribute a change only when the counterfactual holds all other factors fixed. Otherwise write `net change after introducing X and re-optimizing`; this is a **因果归因** boundary.

## Decomposition proof

Before calling a partition lossless, inspect every objective term and constraint for cross-block variables. A decomposition is valid only when all couplings are absent, separable, or handled by a justified coordination variable/dualization. Disjoint crop sets can justify land-type separation even when market-frequency constraints couple plots inside each type; "constraints only act within plots" cannot.

## Synchronization gate

After changing any claim in the body, search and reconcile the abstract, conclusion, captions, tables, and figures. A cautious body sentence paired with an overstated abstract still fails review.

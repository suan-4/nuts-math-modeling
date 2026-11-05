# Physical, Geometric, Simulation, and Inverse Problems

## Establish the system

- Define object, geometry, coordinate system, orientation, time origin, sign convention, and units.
- State initial, boundary, interface, and continuity conditions.
- Tie every simplification to the mechanism it removes.
- Use diagrams when spatial, force, optical, motion, or interface relations are hard to verify from prose.

## Derive rather than announce

Recommended chain:

1. Identify governing law or geometric invariant.
2. Translate it into variables defined for this problem.
3. Derive the governing equation or recurrence.
4. State domain and conditions for a unique/usable solution.
5. Choose numerical method from the equation's structure.
6. Report intermediate states needed to reproduce the final quantity.
7. Convert coordinates/units only with an explicit transformation.

Do not let a numerical solver replace the physical model. The reader must know what equation is solved.

## Inverse problems

- Identify observed quantity, latent parameter, forward model, residual/objective, identifiability, and initialization.
- Explain why the observations contain enough information for the parameter.
- Report uncertainty or variation across observations, not only one fitted value.
- When possible, use a second independent route to cross-check the inverse solution.

## Validation hierarchy

Use the strongest available:

- dimensional analysis;
- boundary and limiting cases;
- conservation law;
- analytic special case;
- grid/time-step convergence;
- independent derivation or solution route;
- simulation/experiment comparison;
- parameter sensitivity and uncertainty propagation.

State what each test supports. Grid convergence supports numerical stability, not necessarily physical truth.

When an initially uniform profile conflicts with the immediate boundary flux, include startup and boundary locations in a full-time error search. Distinguish environment sampling interval, internal time step, saved output interval and spatial export interval. A dense output workbook is not proof of a correspondingly fine internal solution.

For shrinking bodies distinguish fixed physical positions from material coordinates and a moving surface; an out-of-domain point has no material-state value. Derive the chain rule and material velocity before choosing whether an advection term remains. Do not count the same motion twice.

For continuous decreasing states under a strict threshold, an infimum of the admissible times can occur at equality and need not itself satisfy the strict inequality. Distinguish that threshold-crossing limit, the first discrete passing time and the first saved row. Do not silently change `<` to `<=` to match rounded display values.

## Correction models

When adding a more complex mechanism:

1. Derive a criterion for when the omitted effect is important.
2. Evaluate the criterion on current data.
3. Apply the correction only where needed.
4. Compare corrected and base results.
5. Explain whether the correction changes the requested conclusion.

## Result presentation

Apply [figure-table-workflow.md](figure-table-workflow.md) to geometry diagrams, fitted curves, convergence histories, state snapshots, and exact result tables. Use formula-identical symbols and fixed axes across dynamic panels.

Separate:

- model equation and assumptions;
- solution procedure and settings;
- result table/curve;
- physical interpretation;
- validation and applicable range.

Report position/time/velocity/thickness/temperature with consistent units and precision. Label coordinate frame and whether values are signed, magnitudes, averages, or extrema.

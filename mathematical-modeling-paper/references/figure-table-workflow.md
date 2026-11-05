# Figure and Table Workflow

Treat figures and tables as evidence, not decoration or raw software output.

`claim -> source result -> evidence form -> figure/table -> quantitative interpretation -> next decision`

## Choose the evidence form

| Reader need | Default |
|---|---|
| Retrieve exact values, parameters, schedules, or recommendations | table |
| See trend, shape, distribution, uncertainty, anomaly, or convergence | figure |
| Understand mechanism, geometry, or execution logic | diagram |
| See pattern and retrieve selected values | figure plus compact table |

Use both only when they answer different questions. Do not duplicate every plotted point in a table.

## Chart-selection gate

Write one testable claim before choosing the chart: `this evidence shows [relation], so [next model choice or conclusion]`. If the claim cannot be stated, do not plot yet.

| Evidence need | Use | Do not use by default |
|---|---|---|
| Physical geometry, spatial interaction, trajectory, occlusion | scale-aware schematic, trajectory view, cross-section, projection, or fixed-time snapshots | decorative 3-D rendering without labels or a computable relation |
| Exact comparison across categories | sorted horizontal bars, grouped bars, dot plot, or compact table | 3-D bars, perspective effects, or unrelated gradients |
| Composition of a whole | pie/donut only for <=5-6 mutually exclusive categories totaling 100% | 3-D/exploded pie; pie when values are close, categories are many, or groups/times must be compared |
| Time coverage, handoff, schedule, allocation | timeline, Gantt/swimlane, or interval plot | a line chart that conceals start/end and overlap |
| Parameter response, threshold, sensitivity | response curve with baseline, range, threshold, and feasible region | a dense plot with only a legend and no decision point |
| Matrix, spatial field, correlation, or parameter grid | heatmap with explicit axes, scale, normalization, and key-region annotation | colorized raw table without an interpretable structure |
| Multidimensional profile | radar only for normalized, commensurate metrics and few objects; otherwise heatmap/bars | overlapping radar polygons or area comparison as numerical proof |

Use 3-D only when a third meaningful variable (including time plus radius plus state) carries evidence and perspective helps. Avoid a 3-D surface that conceals boundaries, scalar values or late-stage variation; a 2-D heatmap, sections or small multiples may communicate it better.

## Bizard source-code routing

When installed and useful, the `bizard` gallery can supply reference plotting patterns. Search by the intended claim and data structure, not visual novelty. This skill must also work without it; do not force an external gallery lookup for a simple established curve or flowchart.

Apply this sequence:

1. State the figure's testable claim, exact source result, variables, units, and downstream decision.
2. Map that need to a Bizard category and shortlist two or three examples from the CSV using `Type`, `Level1`, `Level2`, `Name`, and `Description`.
3. Open the linked full tutorial and inspect the actual source code, dependencies, data transformations, statistical assumptions, and license attribution before adapting it.
4. Replace all tutorial/sample data with the competition's canonical result artifact. Remove irrelevant biomedical semantics and do not preserve labels, thresholds, tests, or transformations that are unsupported by the current problem.
5. Simplify the visual to the paper's typography, final insertion size, stable semantic colors, and grayscale requirements. Submitted code should declare dependencies rather than attempt online package installation during evaluation.
6. Recompute and reconcile every displayed value, statistic, ordering, annotation, and threshold with the canonical result artifact; then inspect the exported figure at Word/PDF size.

Bizard is a code and design reference, not evidence for the mathematical result. It does not replace custom physical trajectories, geometry/mechanism diagrams, optimization feasible-region views, or modeling flowcharts when those are what the claim requires. Do not add a chart merely because a polished example exists.

Verify the actual license of any borrowed tutorial or code. Retain required attribution and source URLs; do not redistribute a gallery or third-party template as team-authored material.

## Figure contract

Before plotting record: claim, subproblem, exact source, role, selected type, encodings, units, invariants, lead-in sentence, caption, downstream use, plotting source, and deliverables.

Route common evidence needs:

- mechanism/geometry: labeled schematic with formula-identical symbols;
- algorithm: flowchart whose node names match numbered steps;
- fit/assumptions: observed-fitted, residual, Q-Q, calibration, and numerical metric as needed;
- optimization: objective/response curve plus direct feasibility evidence;
- dynamics: fixed-scale small multiples or state snapshots;
- classification: threshold plot, confusion matrix, and subgroup/error view;
- sensitivity: response curve with baseline, range, threshold, and uncertainty.

For every physical/geometry figure, enforce `define symbols -> show labeled configuration -> identify the relation -> derive the matching formula`. A flowchart cannot replace a mechanism diagram. For a multi-question overview, every arrow must carry a prior result, constraint, or decision rather than merely connect method names.

## Style hierarchy

- Use color only for a stable variable role such as object, state, or magnitude. Keep labels and annotations black; make the main evidence darkest and guides/backgrounds lightest.
- Use a restrained palette with sufficient contrast at final size. Background fills can be pale while foreground red/blue curves remain saturated enough to distinguish. Do not force all colors to be pale; check grayscale and color-vision accessibility.
- Prefer direct labels, a small number of purposeful markers, and light reference lines. Add an inset only when a documented local feature cannot be read at final size.
- Keep same-object colors, line widths, marker logic, coordinate conventions, and typography consistent throughout the paper. Do not use visual novelty as a reason to introduce a chart type.
- Avoid decorative rounded-card flowcharts, generic software screenshots, strong background art, 3-D pie/column charts, and other effects that reduce numerical or spatial readability.

## Structured modeling flowcharts

Use a flowchart only to show a real modelling or solution dependency. It must make the reader see what enters a stage, what operation is performed, what is verified, and what proceeds to the next stage. Do not compress body paragraphs into boxes.

For a multi-question paper one overall route near problem analysis is often enough. Add a per-question chart only when its branching, coupling or iteration cannot be explained clearly by the overall chart and short prose. Do not automatically create one chart per question.

### Layout contract

1. Plan the hierarchy before drawing: `outer frame -> 2 to 4 functional groups -> nodes -> connectors`.
2. For the approved grouped style, use a solid outer frame and **虚线分组框** for functional layers. Other clear layouts are allowed. A group label needs a reserved **标题带**; do not place a node under or through the label.
3. Use **单图单主题色**: one low-saturation theme color for that chart's borders, arrows, dotted groups, and restrained emphasis fill. Different charts may use different theme colors. Do not mix several semantic colors inside one process chart without a data meaning.
4. Use white nodes by default and reserve the single theme's darker fill for the main model, transformation, or final merged result. Keep node labels short noun phrases or verb phrases, never formula blocks or full explanatory sentences.
5. Use **直角折线** connectors. A connector must leave and enter at a **节点边界**, use a shared trunk before parallel branches, and never cross a node, its text, another arrowhead, or a group title. Do not use diagonal arrows.
6. Give each question chart a different internal topology when the mathematics differs: e.g., direct solve, parallel land-type decomposition, or two-input linearization. Do not recycle a generic vertical stack merely by renaming boxes.

### Mandatory visual QA

Inspect every flowchart at original export size and at Word insertion size before accepting it. Check, in order: paper title versus outer frame; every group title versus first-row nodes; node text versus borders; arrowheads versus targets; branches versus each other; dashed group boundaries; and final caption/page placement. If any collision appears, repair the source layout coordinates and regenerate the image; never paint over the bitmap.

## Figure evidence contract

Before accepting a figure, verify all of the following:

1. The title/caption identifies object, condition, quantity, and unit where applicable.
2. Axes, coordinates, time origin, sign convention, symbols, and thresholds agree with the formula and code.
3. The plotted result reconciles with the canonical artifact, including extrema, selected values, intervals, allocations, and feasibility margins.
4. The body contains a lead-in, a quantitative interpretation, and the decision or later step that uses the evidence.
5. The figure contributes a distinct proof role; it does not repeat a neighboring figure or table.
6. Original-size and Word insertion-size reviews both show legible text, no collision/clipping, meaningful whitespace, and a grayscale-readable encoding.

A convergence curve supports the stated stopping condition. It does not prove global optimality.

## Table contract

Use definition/input, descriptive/preprocessing, parameter, method-comparison, validation, robustness, or final-result tables according to role.

Required checks:

- title states object, condition, and metric;
- row/column meaning, units, denominators, sorting, and missing-value codes are explicit;
- precision follows measurement or decision sensitivity rather than raw program output;
- uncertainty labels distinguish SD, SE, IQR, and confidence intervals;
- totals, extrema, rankings, constraints, and highlighted cells are recomputed;
- full machine-oriented output moves to an appendix or attachment.

Use a clean three-line table by default, avoid vertical rules, place units in headers, align numeric columns, explain abbreviations and highlighting in notes, and never shrink text below readable size merely to fit the page.

For an official answer template, preserve its requested headers, order, merged cells, units and grid structure; it takes precedence over the default three-line style. Do not delete a required result column to improve appearance. In a shrinking domain, a fixed physical radius outside the current body has no material state, while the moving surface still does. Explain an em dash/blank and the current radius; omit an all-outside column from a compact body table only when authorized and allowed by the problem, retaining the required full result export.

Repeat headers on continuation pages; avoid a caption stranded above an empty table or a final row floating alone. Do not add units redundantly in both caption and header. Numeric scientific notation should use professional superscripts, not literal caret or formula-conversion residue.

## Code appendices

Generate code listings from the submitted runnable source. Use the selected template's code font, size and frame requirements; this project's profile uses a surrounding box, Times New Roman 小五9pt, single spacing and per-question titles. Monospaced fonts or line numbers are options for other templates, not automatic overrides. Preserve indentation and source order, repeat the listing title on continuation pages, and inspect wrapping and the final page. Never manually edit only the paper copy of a path statement.

## Formula-text integration

Every important figure or table needs:

1. a lead-in explaining why the evidence is needed;
2. a self-contained caption/title;
3. a result sentence extracting a value, trend, threshold, exception, or relation;
4. a decision sentence stating what model, parameter, constraint, or next step follows.

For geometry use `define symbols -> diagram -> identify relation -> derive formula`. For diagnostics use `state condition -> diagnostic evidence -> quantitative result -> modeling consequence`.

## Canonical source and numerical QA

Generate every related figure and table from one canonical result artifact. Record filters, transformations, sample counts, units, axis transforms, ordering, binning, smoothing, seeds, and uncertainty calculations.

Independently compare plotted/table extrema, selected values, thresholds, category counts, objectives, constraints, and metrics with raw arrays or recomputation. Keep unrounded values for calculation and round only for display.

## Visual and page QA

Export reproducible source plus editable SVG and final PDF/PNG where applicable. Render the manuscript and inspect at final PDF size for:

- unreadable or clipped text, labels, legends, notes, or Chinese glyphs;
- inconsistent axes, semantic colors, units, symbols, and panel labels;
- detached captions, figures before definition, or tables separated from interpretation;
- color-only meaning, poor grayscale behavior, low resolution, and excessive decoration;
- wide tables, broken continuation headers, ambiguous blanks, and inconsistent precision.

## Automatic repair

For a confirmed defect:

1. preserve the original export and source;
2. record the visual, semantic, or numerical failure;
3. repair plotting/table-generation source rather than the bitmap or pasted cells;
4. perform automatic redraw and automatic table regeneration;
5. rerun numerical reconciliation;
6. rerender the final PDF page;
7. synchronize captions, titles, notes, body, abstract, and conclusion when mapping is unambiguous.

If source data or intended claim is ambiguous, stop before choosing a visual interpretation silently.

## Efficient plotting sequence learned from this project

1. Decide the one question a figure answers. Lock its source, axes, required times/positions, key-point values and approximate insertion size before styling.
2. Reuse an approved style configuration: fonts, curve colors, line widths, marker logic, axes frame and captions. Reuse style, not an identical topology for every different diagram.
3. Render one representative figure first. Check Chinese glyphs, mathematical labels, numerical reconciliation and final paper size before expanding to the entire series.
4. Make one source-level repair per confirmed issue. After approval, freeze the layout or record the user's manual dimensions; do not continue cosmetic variants when the user wants the next modeling step.
5. Render at export size and insertion size, inspect all labels/arrows, then insert and check the actual PDF page. Tight layout alone does not prove absence of overlap.

### Concrete curve and surface fixes

- Align markers with actual table sampling times. This project's key points use slightly enlarged stars in the same color as the curve; do not mark every internal step.
- Label the endpoint time explicitly and give it visual priority. Route the leader with space around it; check against reference lines and other curves. A short vertical/horizontal segment is often clearer than a long diagonal.
- A legend entry is required for each semantically different visible curve, fill or reference line. Unrelated right-side regions stay unfilled. Avoid an unexplained blue segment or colors that merge into the background.
- Dense profiles should use selected times, small multiples or a **separate adjacent** zoom panel when the user requests it. Keep late-time detail readable without hiding the early-time context.
- Separate temperature and moisture surfaces when their scales or perspective make a combined panel too small. Check front/back boundary artifacts, apparent gaps from mesh sampling, and clipped colorbar/axis labels.
- Four-sided axes borders, legend placement and semantic colors should match the approved series. Layout can change to serve different evidence; consistency is not copying the same panel composition.

### Concrete geometry and flowchart fixes

- Cylinders must be recognizably cylindrical. Use stated dimensions and scale, or explicitly label a schematic not to scale; do not draw a short squat cylinder for a long slender object without explanation.
- A radius label such as `R=2cm` belongs on the actual center-to-edge radius. Enlarge/reposition the geometry to fit the label rather than placing it outside an ambiguous arrow. Solid/dashed lines must have explained roles.
- Flowchart labels name inputs, model steps, numerical operations, checks and outputs. Keep them short; avoid formulas and attachment-number clutter in the overview.
- Plan arrow corridors before enlarging text. Parallel branches share trunks; connect arrowheads to a segment in the same direction; end at the node boundary. Move boxes to make room, not arrowheads into the text.
- Decision labels “是/否” need reserved space beside the branch and must not cover its line. Side strip labels can be one character per line; check them independently of box labels.
- Use final insertion aspect ratio early. Shrinking a very wide chart into one narrow page makes even large export fonts unreadable. Re-layout compactly with actual arrow space, not arbitrary whitespace.

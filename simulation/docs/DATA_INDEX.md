# Simulation data and code index

Numerical paths below are relative to the simulation directory. The [Extended Companion](../../documents/extended.pdf) is included. The manuscript and Technical Supplement are submitted separately and are not included in this repository. Methods C01–C09 and Tables C1–C4 use their own identifiers. Computational reconstruction does not replace the complete proofs in the manuscript and Technical Supplement.

| Evidence location | Computational methods | Principal data and code |
|---|---|---|
| Main Figure 2(a)–(b), time histories | [C04](COMPUTATIONAL_COMPANION.html#c04-main), [C03](COMPUTATIONAL_COMPANION.html#c03) | `data/figure_series/deterministic_timeseries.csv`; `code/figure_series.py` |
| Main Figure 2(c), terminal-phase distance | [C05](COMPUTATIONAL_COMPANION.html#c05) | `data/records/phase_map_validation.csv`; `targeted/phase_reference.py` |
| Main Figure 3(a)–(b), scalar accuracy and ratios | [C09](COMPUTATIONAL_COMPANION.html#c09-scalar) | `data/figure_series/optimized_noise_scaling.csv`; `code/schedule_noise.py` |
| Main Figure 3(c), nonlinear network means | [C06](COMPUTATIONAL_COMPANION.html#c06) | `data/statistics/stochastic_cap_statistics.csv`; `code/stochastic_reporting.py` |
| Technical Supplement Figure S1, local certificate | [C08](COMPUTATIONAL_COMPANION.html#c08) | `data/figure_series/local_certified_trajectory.csv`; `code/local_certificate.py` |
| Technical Supplement Figure S2, displacement | [C04](COMPUTATIONAL_COMPANION.html#c04-displacement) | `data/records/tangential_scaling.csv`; `targeted/protocol_reference.py` |
| Technical Supplement Figure S3, paired contrasts | [C06](COMPUTATIONAL_COMPANION.html#c06-paired) | `data/statistics/stochastic_cap_statistics.csv`; `code/table_reporting.py` |
| Extended Companion Figure R1, graph rates | [C04](COMPUTATIONAL_COMPANION.html#c04-graphs) | `data/records/exponent_validation.csv`; `targeted/protocol_reference.py` |
| Main Table II | [Table C1](COMPUTATIONAL_COMPANION.html#table-c1) | `data/records/comparison_metrics.csv` |
| Complete cap comparisons | [Table C2](COMPUTATIONAL_COMPANION.html#table-c2) | `data/statistics/stochastic_cap_statistics.csv` |
| Dependent coarse/fine comparison | [Table C3](COMPUTATIONAL_COMPANION.html#table-c3) | `data/statistics/stochastic_step_statistics.csv` |
| Pathwise extrapolation | [Table C4](COMPUTATIONAL_COMPANION.html#table-c4) | `data/statistics/stochastic_richardson_statistics.csv` |

Main Figure 1 and Extended Companion Figure R2 are geometric schematics. Main Table I is the selected-literature comparison. They are not numerical datasets. The submitted Technical Supplement contains all five complete supporting proofs.

## Section asset directory

### C01 — Model, metric and experiment families

[Companion location](COMPUTATIONAL_COMPANION.html#c01)

- [`docs/MODEL.md`](../docs/MODEL.md)
- [`docs/NUMERICAL_PROTOCOL.md`](../docs/NUMERICAL_PROTOCOL.md)
- [`config/experiments.json`](../config/experiments.json)
- [`code/network_experiments.py`](../code/network_experiments.py)
- [`code/stochastic_network.py`](../code/stochastic_network.py)

### C02 — Deterministic schedules and complete comparison

[Companion location](COMPUTATIONAL_COMPANION.html#c02)

- [`data/records/comparison_metrics.csv`](../data/records/comparison_metrics.csv)
- [`data/records/method_metrics.csv`](../data/records/method_metrics.csv)
- [`data/records/functional_hierarchy_values.csv`](../data/records/functional_hierarchy_values.csv)
- [`data/figure_series/comparison_metrics.csv`](../data/figure_series/comparison_metrics.csv)

### C03 — Full-clock energy and phase diagnostics

[Companion location](COMPUTATIONAL_COMPANION.html#c03)

- [`data/targeted_reference/effort/full_clock_snapshot.csv`](../data/targeted_reference/effort/full_clock_snapshot.csv)
- [`data/targeted_reference/effort/full_clock_cutoff_series.csv`](../data/targeted_reference/effort/full_clock_cutoff_series.csv)
- [`data/targeted_reference/protocols/full_clock_phase_grid.csv`](../data/targeted_reference/protocols/full_clock_phase_grid.csv)
- [`targeted/effort_reference.py`](../targeted/effort_reference.py)

### C04 — Contraction, graph and displacement protocols

[Companion location](COMPUTATIONAL_COMPANION.html#c04)

- [`data/records/exponent_validation.csv`](../data/records/exponent_validation.csv)
- [`data/records/tangential_scaling.csv`](../data/records/tangential_scaling.csv)
- [`data/targeted_reference/protocols/graph_protocol_and_reintegration.csv`](../data/targeted_reference/protocols/graph_protocol_and_reintegration.csv)
- [`data/targeted_reference/protocols/displacement_protocol_and_reintegration.csv`](../data/targeted_reference/protocols/displacement_protocol_and_reintegration.csv)
- [`targeted/protocol_reference.py`](../targeted/protocol_reference.py)

### C05 — Terminal-phase curve and endpoint diagnostics

[Companion location](COMPUTATIONAL_COMPANION.html#c05)

- [`data/records/phase_map_validation.csv`](../data/records/phase_map_validation.csv)
- [`data/figure_series/phase_map_validation.csv`](../data/figure_series/phase_map_validation.csv)
- [`data/targeted_reference/phase/phase_reference.json`](../data/targeted_reference/phase/phase_reference.json)
- [`targeted/phase_reference.py`](../targeted/phase_reference.py)

### C06 — Complete primary stochastic cap evidence

[Companion location](COMPUTATIONAL_COMPANION.html#c06)

- [`data/records/stochastic_crn_pathwise_terminal_mse.npz`](../data/records/stochastic_crn_pathwise_terminal_mse.npz)
- [`data/statistics/stochastic_cap_statistics.csv`](../data/statistics/stochastic_cap_statistics.csv)
- [`data/records/stochastic_summary.json`](../data/records/stochastic_summary.json)
- [`code/table_reporting.py`](../code/table_reporting.py)

### C07 — Covariance-aware vertex and nested refinement

[Companion location](COMPUTATIONAL_COMPANION.html#c07)

- [`data/statistics/stochastic_quadratic_fit.json`](../data/statistics/stochastic_quadratic_fit.json)
- [`data/statistics/stochastic_step_statistics.csv`](../data/statistics/stochastic_step_statistics.csv)
- [`data/statistics/stochastic_richardson_statistics.csv`](../data/statistics/stochastic_richardson_statistics.csv)
- [`data/statistics/stochastic_sample_split.csv`](../data/statistics/stochastic_sample_split.csv)
- [`targeted/statistics_reference.py`](../targeted/statistics_reference.py)

### C08 — Numerical evaluation of analytic certificates

[Companion location](COMPUTATIONAL_COMPANION.html#c08)

- [`data/records/local_certificate.json`](../data/records/local_certificate.json)
- [`data/records/local_initial_states.csv`](../data/records/local_initial_states.csv)
- [`data/records/local_solver_comparison.csv`](../data/records/local_solver_comparison.csv)
- [`data/records/local_trajectory.csv`](../data/records/local_trajectory.csv)
- [`data/figure_series/local_certified_trajectory.csv`](../data/figure_series/local_certified_trajectory.csv)
- [`code/benchmark_certificate.py`](../code/benchmark_certificate.py)

### C09 — Scalar and modal diagnostic records and supersessions

[Companion location](COMPUTATIONAL_COMPANION.html#c09)

- [`data/records/modal_lambert_remainder_and_slopes.csv`](../data/records/modal_lambert_remainder_and_slopes.csv)
- [`data/records/asymptotic_power_p3_accuracy.csv`](../data/records/asymptotic_power_p3_accuracy.csv)
- [`data/targeted_reference/power/historical_power_p3_accuracy.csv`](../data/targeted_reference/power/historical_power_p3_accuracy.csv)
- [`data/targeted_reference/power/power_p3_successor.csv`](../data/targeted_reference/power/power_p3_successor.csv)
- [`config/supersession.json`](../config/supersession.json)
- [`targeted/power_reference.py`](../targeted/power_reference.py)


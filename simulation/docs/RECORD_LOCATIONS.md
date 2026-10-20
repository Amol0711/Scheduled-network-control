# Record locations

The [Extended Companion](../../documents/extended.pdf) is supplied here. The manuscript and Technical Supplement are submitted separately, not included as repository files. References to their figures, sections and equations below identify the results supported by these simulations. This computational document uses sections C01–C09, equations E01–E10, and Tables C1–C4 independently of the article numbering.

| Article location or quantity | Methods location | Numerical record |
|---|---|---|
| Main Table II | [Table C1](COMPUTATIONAL_COMPANION.html#table-c1) | `data/records/comparison_metrics.csv` |
| Main Figure 3(c), Technical Supplement Figure S3 | [Table C2](COMPUTATIONAL_COMPANION.html#table-c2) | `data/statistics/stochastic_cap_statistics.csv` |
| Technical Supplement IV-D, step sensitivity | [Table C3](COMPUTATIONAL_COMPANION.html#table-c3) | `data/statistics/stochastic_step_statistics.csv` |
| Dependent extrapolation diagnostic | [Table C4](COMPUTATIONAL_COMPANION.html#table-c4) | `data/statistics/stochastic_richardson_statistics.csv` |
| Technical Supplement (S25)–(S27), mean and marginal interval | E07, [C06](COMPUTATIONAL_COMPANION.html#c06-estimands) | Terminal path arrays and reporting module |
| Technical Supplement (S28), paired intervals | E08, [C06](COMPUTATIONAL_COMPANION.html#c06-paired) | Same primary paths, fifteen nonreference contrasts |
| Extrapolation and covariance | E09–E10, [C07](COMPUTATIONAL_COMPANION.html#c07-richardson) | Nested coarse/fine paths, not independent samples |
| Technical Supplement (S20), local bound | [C08](COMPUTATIONAL_COMPANION.html#c08-trajectory) | `data/records/local_summary.json` |
| Extended Figure R1 and Technical Supplement Figure S2 | [C04](COMPUTATIONAL_COMPANION.html#c04) | Recorded grids, initial states, and masks |
| Main Figure 2(c), phase distance | [C05](COMPUTATIONAL_COMPANION.html#c05) | Raw phase curve and separate transported-endpoint diagnostics |
| Main Figure 3(a)–(b), Extended I-B–I-D | [C09](COMPUTATIONAL_COMPANION.html#c09) | Scalar/modal diagnostics and high-precision power reference |

The full sixteen-cap table includes the unresolved near-reference contrasts and the exactly zero reference. The recorded p=3 optimizer and its high-precision comparison retain separate numerical provenance.

# Prescribed-time control — simulations and extended supplement

Reproducibility materials for **Prescribed-Time Control Beyond Equilibria with Terminal Phase Guarantees**.

This repository contains simulation programs, experiment configurations, recorded numerical data, plotting inputs, computational methods, and the extended supplement. 

## Read the materials

- [Extended Analysis and Reproducibility Companion](documents/extended.pdf) — four pages of additional analytical refinements and secondary illustrations.
- [Computational methods](simulation/docs/COMPUTATIONAL_COMPANION.pdf) — simulation methods C01–C09 and complete numerical tables C1–C4, also available as [HTML](simulation/docs/COMPUTATIONAL_COMPANION.html) and [Markdown](simulation/docs/COMPUTATIONAL_COMPANION.md).
- [Simulation data and code index](simulation/docs/DATA_INDEX.html), [record locations](simulation/docs/RECORD_LOCATIONS.html), and [execution guide](docs/EXECUTION_SCOPE.md).

References marked “main” or “Technical Supplement” refer to the separately submitted documents. In the extended PDF those references are ordinary printed identifiers, not links to missing local files. Its own section, equation and figure links remain active. The computational methods use their own C/E identifiers.

## Contents

| Location | Material |
|---|---|
| `documents/extended.pdf` | Extended supplement. This is the only file in `documents/`. |
| `simulation/code/` | Numerical kernels and computation checks. |
| `simulation/config/` | Fixed experiment settings, tested environment and numerical input bindings. |
| `simulation/data/` | Numerical tables, recorded trajectories, terminal path arrays and independent precision checks. |
| `simulation/targeted/` | High-precision and deterministic reference calculations. |
| `simulation/docs/` | User-facing model, numerical protocol, computational methods and data indexes. |
| `data/plotting/` | Twelve publication plotting CSVs. |
| `tools/` | Two display-only plotting-data exporters. |

## Check integrity without running experiments

Run these commands from the extracted repository root:

```bash
python3 -B verify_repository.py
python3 -B simulation/reproduce.py verify
```

Both commands are read-only and use the Python standard library. They verify supplied checksums and file membership. Always specify `verify`: invoking the numerical launcher without a mode selects `quick`, which reconstructs statistics and writes results.

## Reproduce the numerical studies

The tested interpreter is CPython 3.13.5 on Linux x86_64. Dependency pins are in `simulation/requirements.txt`; these are reproducibility settings, not latest-version recommendations. Install dependencies and write all results outside this repository.

```bash
python3.13 -m venv ../simulation_env
../simulation_env/bin/python -m pip install -r simulation/requirements.txt
../simulation_env/bin/python -B simulation/reproduce.py quick --output-dir ../results
```

Read [simulation/README.txt](simulation/README.txt) and the [execution guide](docs/EXECUTION_SCOPE.md) before selecting another mode. `quick` reconstructs statistics and certificate diagnostics without generating trajectories. `deterministic` integrates deterministic trajectories. The stochastic-generation modes require explicit confirmation. The stored NPZ contains terminal squared-disagreement arrays, not all trajectories or Brownian increments.

The original double-precision optimizer records and high-precision comparisons remain separate. Shared-increment paths, the nested refinement population, unresolved contrasts and zero-reference comparisons retain their stated interpretations. Sampling intervals concern fixed-step, fixed-grid estimands. Numerical consistency checks do not constitute rigorous continuous-time error certificates.

## Simulation documentation and plot-data tools

Rebuild the computational-methods editions into a new external directory with Pandoc and pdfLaTeX:

```bash
python3 -B simulation/tools/build_companion.py --output ../methods_build
```

Optional display-only exporters read supplied data and write into new external directories. They do not simulate, fit curves, or reconstruct confidence intervals.

```bash
python3 -B tools/export_deterministic_plot_data.py --source data/plotting --output ../deterministic_display
python3 -B tools/export_accuracy_plot_data.py --root . --out ../accuracy_display --report ../accuracy_display_report.json
```

No audit reports, editorial maps, development versions, manuscript sources, LaTeX auxiliary snapshots, or submission documents are part of this package. Checksums and numerical input bindings are retained to make the simulation files verifiable. No redistribution license is newly granted. Preserve `.gitattributes` to avoid changing data bytes during transfer.

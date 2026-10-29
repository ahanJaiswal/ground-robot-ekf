#!/usr/bin/env python3
"""Plot dead-reckoning output: elapsed_seconds,x_m,y_m,theta_rad.

Usage:
    python3 scripts/plot_trajectory.py
    python3 scripts/plot_trajectory.py results/my_run.csv --show

Requires numpy and matplotlib. Saves a PNG next to the input by default.
"""

import argparse
from pathlib import Path
import sys

import numpy as np


def main():
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path,
                        default=project / "results/dead_reckoning.csv")
    parser.add_argument("--output", type=Path, help="Output PNG path")
    parser.add_argument("--show", action="store_true", help="Open a plot window")
    args = parser.parse_args()
    if not args.csv.is_file():
        parser.error(f"CSV not found: {args.csv}. Generate your trajectory first.")

    required = ("elapsed_seconds", "x_m", "y_m", "theta_rad")
    try:
        data = np.genfromtxt(args.csv, delimiter=",", names=True,
                             dtype=float, encoding="utf-8", ndmin=1)
    except (ValueError, OSError) as exc:
        parser.error(f"Cannot read CSV: {exc}")
    if not data.dtype.names or any(c not in data.dtype.names for c in required):
        parser.error("CSV header must contain: " + ",".join(required))
    if data.size < 2:
        parser.error("At least two trajectory rows are required.")
    values = np.column_stack([data[c] for c in required])
    if not np.isfinite(values).all():
        parser.error("Trajectory contains missing or nonfinite values.")
    t, x, y, theta = values.T
    if np.any(np.diff(t) <= 0):
        parser.error("elapsed_seconds must be strictly increasing.")

    import matplotlib
    if not args.show:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    route, heading = axes
    route.plot(x, y, color="0.75", linewidth=0.8, zorder=1)
    points = route.scatter(x, y, c=t / 60, cmap="viridis", s=5, zorder=2)
    route.scatter(x[0], y[0], color="green", s=65, label="Start", zorder=3)
    route.scatter(x[-1], y[-1], color="red", marker="X", s=65,
                  label="End", zorder=3)
    route.set(xlabel="Local x (m)", ylabel="Local y (m)",
              title="Dead-reckoning trajectory", aspect="equal")
    route.legend()
    fig.colorbar(points, ax=route, label="Elapsed time (min)", shrink=0.8)
    heading.plot(t / 60, np.rad2deg(np.unwrap(theta)), linewidth=1)
    heading.set(xlabel="Elapsed time (min)", ylabel="Unwrapped heading (degrees)",
                title="Estimated heading")
    for ax in axes:
        ax.grid(alpha=0.25)
    output = args.output or args.csv.with_suffix(".png")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180)
    print(f"Saved plot: {output.resolve()}")
    print(f"Samples: {len(t):,}; duration: {(t[-1] - t[0]):.1f} seconds")
    if args.show:
        plt.show()
    plt.close(fig)
    return 0


if __name__ == "__main__":
    sys.exit(main())

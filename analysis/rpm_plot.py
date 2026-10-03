import csv
from pathlib import Path

import matplotlib.pyplot as plt


class RPMPlotter:
    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)

    def load_data(self):
        elapsed = []
        target = []
        measured = []

        with self.csv_path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                elapsed.append(float(row["elapsed_seconds"]))
                target.append(float(row["target_rpm"]))
                measured.append(float(row["measured_rpm"]))

        return elapsed, target, measured

    def create_plot(self, elapsed, target, measured):
        plt.figure(figsize=(10, 6))

        plt.plot(
            elapsed,
            target,
            linestyle="--",
            linewidth=2,
            label="Target RPM"
        )

        plt.plot(
            elapsed,
            measured,
            marker="o",
            linewidth=1.5,
            label="Measured RPM"
        )

        plt.xlabel("Elapsed Time (seconds)")
        plt.ylabel("RPM")
        plt.title("RPM Stability Verification")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        output_path = (
            Path(__file__).resolve().parents[1]
            / "results"
            / "rpm_stability_plot.png"
        )

        plt.savefig(output_path, dpi=300)
        plt.show()

        print(f"Graph saved to: {output_path}")


if __name__ == "__main__":
    csv_file = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "sample_rpm.csv"
    )

    plotter = RPMPlotter(csv_file)

    elapsed, target, measured = plotter.load_data()

    plotter.create_plot(
        elapsed,
        target,
        measured
    )
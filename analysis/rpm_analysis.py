import csv
import math
from pathlib import Path


class RPMAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)
        self.readings = []

    def load_data(self):
        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {self.csv_path}"
            )

        with self.csv_path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.readings.append({
                    "target_rpm": float(row["target_rpm"]),
                    "measured_rpm": float(row["measured_rpm"]),
                    "deviation_rpm": float(row["deviation_rpm"])
                })

        if not self.readings:
            raise ValueError("No RPM readings found.")

    def calculate_statistics(self):
        measured = [
            reading["measured_rpm"]
            for reading in self.readings
        ]

        deviations = [
            reading["deviation_rpm"]
            for reading in self.readings
        ]

        target = self.readings[0]["target_rpm"]

        average_rpm = sum(measured) / len(measured)
        minimum_rpm = min(measured)
        maximum_rpm = max(measured)

        variance = sum(
            (rpm - average_rpm) ** 2
            for rpm in measured
        ) / len(measured)

        standard_deviation = math.sqrt(variance)

        maximum_absolute_deviation = max(
            abs(deviation)
            for deviation in deviations
        )

        mean_absolute_deviation = sum(
            abs(deviation)
            for deviation in deviations
        ) / len(deviations)

        stable_readings = sum(
            1
            for deviation in deviations
            if abs(deviation) <= 5
        )

        stability_percentage = (
            stable_readings / len(deviations)
        ) * 100

        return {
            "number_of_samples": len(measured),
            "target_rpm": target,
            "average_rpm": average_rpm,
            "minimum_rpm": minimum_rpm,
            "maximum_rpm": maximum_rpm,
            "standard_deviation": standard_deviation,
            "maximum_absolute_deviation": maximum_absolute_deviation,
            "mean_absolute_deviation": mean_absolute_deviation,
            "stability_percentage": stability_percentage
        }

    @staticmethod
    def print_report(statistics):
        print()
        print("=" * 50)
        print("RPM STABILITY ANALYSIS")
        print("=" * 50)

        print(
            f"Number of samples: "
            f"{statistics['number_of_samples']}"
        )

        print(
            f"Target RPM: "
            f"{statistics['target_rpm']:.2f}"
        )

        print(
            f"Average RPM: "
            f"{statistics['average_rpm']:.2f}"
        )

        print(
            f"Minimum RPM: "
            f"{statistics['minimum_rpm']:.2f}"
        )

        print(
            f"Maximum RPM: "
            f"{statistics['maximum_rpm']:.2f}"
        )

        print(
            f"Standard deviation: "
            f"{statistics['standard_deviation']:.2f} RPM"
        )

        print(
            f"Maximum absolute deviation: "
            f"{statistics['maximum_absolute_deviation']:.2f} RPM"
        )

        print(
            f"Mean absolute deviation: "
            f"{statistics['mean_absolute_deviation']:.2f} RPM"
        )

        print(
            f"Stability within ±5 RPM: "
            f"{statistics['stability_percentage']:.2f}%"
        )

        print("=" * 50)


if __name__ == "__main__":
    csv_file = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "sample_rpm.csv"
    )

    analyzer = RPMAnalyzer(csv_file)

    analyzer.load_data()

    statistics = analyzer.calculate_statistics()

    analyzer.print_report(statistics)
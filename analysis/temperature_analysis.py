import csv
import math
from pathlib import Path


class TemperatureAnalyzer:
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
                    "target_temperature_c": float(
                        row["target_temperature_c"]
                    ),
                    "measured_temperature_c": float(
                        row["measured_temperature_c"]
                    ),
                    "deviation_c": float(
                        row["deviation_c"]
                    )
                })

        if not self.readings:
            raise ValueError(
                "No temperature readings found."
            )

    def calculate_statistics(self):
        measured = [
            reading["measured_temperature_c"]
            for reading in self.readings
        ]

        deviations = [
            reading["deviation_c"]
            for reading in self.readings
        ]

        target = self.readings[0][
            "target_temperature_c"
        ]

        average_temperature = (
            sum(measured) / len(measured)
        )

        minimum_temperature = min(measured)

        maximum_temperature = max(measured)

        variance = sum(
            (
                temperature
                - average_temperature
            ) ** 2
            for temperature in measured
        ) / len(measured)

        standard_deviation = math.sqrt(
            variance
        )

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
            if abs(deviation) <= 0.2
        )

        stability_percentage = (
            stable_readings
            / len(deviations)
        ) * 100

        return {
            "number_of_samples": len(measured),
            "target_temperature": target,
            "average_temperature":
                average_temperature,
            "minimum_temperature":
                minimum_temperature,
            "maximum_temperature":
                maximum_temperature,
            "standard_deviation":
                standard_deviation,
            "maximum_absolute_deviation":
                maximum_absolute_deviation,
            "mean_absolute_deviation":
                mean_absolute_deviation,
            "stability_percentage":
                stability_percentage
        }

    @staticmethod
    def print_report(statistics):
        print()
        print("=" * 55)
        print("TEMPERATURE STABILITY ANALYSIS")
        print("=" * 55)

        print(
            f"Number of samples: "
            f"{statistics['number_of_samples']}"
        )

        print(
            f"Target temperature: "
            f"{statistics['target_temperature']:.3f} °C"
        )

        print(
            f"Average temperature: "
            f"{statistics['average_temperature']:.3f} °C"
        )

        print(
            f"Minimum temperature: "
            f"{statistics['minimum_temperature']:.3f} °C"
        )

        print(
            f"Maximum temperature: "
            f"{statistics['maximum_temperature']:.3f} °C"
        )

        print(
            f"Standard deviation: "
            f"{statistics['standard_deviation']:.3f} °C"
        )

        print(
            f"Maximum absolute deviation: "
            f"{statistics['maximum_absolute_deviation']:.3f} °C"
        )

        print(
            f"Mean absolute deviation: "
            f"{statistics['mean_absolute_deviation']:.3f} °C"
        )

        print(
            f"Stability within ±0.2 °C: "
            f"{statistics['stability_percentage']:.2f}%"
        )

        print("=" * 55)


if __name__ == "__main__":
    csv_file = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "sample_temperature.csv"
    )

    analyzer = TemperatureAnalyzer(
        csv_file
    )

    analyzer.load_data()

    statistics = analyzer.calculate_statistics()

    analyzer.print_report(statistics)
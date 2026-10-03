import csv
from pathlib import Path


class TemperatureVerifier:
    def __init__(
        self,
        csv_path,
        pass_limit=0.2,
        warning_limit=0.5
    ):
        self.csv_path = Path(csv_path)
        self.pass_limit = pass_limit
        self.warning_limit = warning_limit
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
                    "measured_temperature_c":
                        float(
                            row["measured_temperature_c"]
                        ),
                    "deviation_c":
                        float(row["deviation_c"])
                })

        if not self.readings:
            raise ValueError(
                "No temperature readings found."
            )

    def calculate_verification(self):
        deviations = [
            reading["deviation_c"]
            for reading in self.readings
        ]

        absolute_deviations = [
            abs(deviation)
            for deviation in deviations
        ]

        maximum_deviation = max(
            absolute_deviations
        )

        if maximum_deviation <= self.pass_limit:
            status = "PASS"

        elif maximum_deviation <= self.warning_limit:
            status = "WARNING"

        else:
            status = "FAIL"

        return {
            "maximum_deviation":
                maximum_deviation,
            "status":
                status
        }


def print_results(results):
    print(
        f"{results['maximum_deviation']:.3f}"
        f" °C"
        f"{results['status']:>15}"
    )


if __name__ == "__main__":
    results_folder = (
        Path(__file__).resolve().parents[1]
        / "results"
    )

    scenarios = [
        "normal_temperature.csv",
        "temperature_drift_temperature.csv",
        "high_temperature_temperature.csv",
        "low_temperature_temperature.csv",
        "noisy_sensor_temperature.csv"
    ]

    print()
    print("=" * 75)
    print("AUTOMATIC TEMPERATURE VERIFICATION")
    print("=" * 75)

    print(
        f"{'Scenario':25}"
        f"{'Max Dev.':15}"
        f"{'Status':15}"
    )

    print("-" * 75)

    for filename in scenarios:
        file_path = results_folder / filename

        verifier = TemperatureVerifier(
            file_path
        )

        verifier.load_data()

        result = verifier.calculate_verification()

        scenario_name = (
            filename
            .replace("_temperature.csv", "")
            .upper()
        )

        print(
            f"{scenario_name:25}"
            f"{result['maximum_deviation']:>8.3f} °C"
            f"{result['status']:>12}"
        )

    print("=" * 75)

    print()
    print(
        "Project verification thresholds:"
    )
    print(
        "PASS    : Maximum deviation <= 0.2 °C"
    )
    print(
        "WARNING : Maximum deviation <= 0.5 °C"
    )
    print(
        "FAIL    : Maximum deviation > 0.5 °C"
    )

    print()
    print(
        "These are project-defined engineering"
    )
    print(
        "test thresholds, not manufacturer limits."
    )
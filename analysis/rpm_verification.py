import csv
from pathlib import Path


class RPMVerification:
    def __init__(
        self,
        deviation_pass=5.0,
        deviation_warning=10.0,
        std_warning=5.0
    ):
        self.deviation_pass = deviation_pass
        self.deviation_warning = deviation_warning
        self.std_warning = std_warning

    def load_data(self, csv_path):
        readings = []

        with open(
            csv_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                readings.append({
                    "measured_rpm": float(row["measured_rpm"]),
                    "deviation_rpm": float(row["deviation_rpm"])
                })

        return readings

    def calculate_statistics(self, readings, target_rpm):
        measured = [
            item["measured_rpm"]
            for item in readings
        ]

        deviations = [
            item["deviation_rpm"]
            for item in readings
        ]

        average_rpm = sum(measured) / len(measured)

        minimum_rpm = min(measured)

        maximum_rpm = max(measured)

        maximum_deviation = max(
            abs(value)
            for value in deviations
        )

        mean_absolute_deviation = sum(
            abs(value)
            for value in deviations
        ) / len(deviations)

        variance = sum(
            (value - average_rpm) ** 2
            for value in measured
        ) / len(measured)

        standard_deviation = variance ** 0.5

        return {
            "target_rpm": target_rpm,
            "average_rpm": average_rpm,
            "minimum_rpm": minimum_rpm,
            "maximum_rpm": maximum_rpm,
            "maximum_deviation": maximum_deviation,
            "mean_absolute_deviation": mean_absolute_deviation,
            "standard_deviation": standard_deviation
        }

    def determine_status(self, statistics):
        maximum_deviation = statistics["maximum_deviation"]
        standard_deviation = statistics["standard_deviation"]

        if (
            maximum_deviation <= self.deviation_pass
            and standard_deviation <= self.std_warning
        ):
            return "PASS"

        if (
            maximum_deviation <= self.deviation_warning
            and standard_deviation <= self.std_warning
        ):
            return "WARNING"

        return "FAIL"

    def verify_file(self, csv_path):
        readings = self.load_data(csv_path)

        if not readings:
            raise ValueError(
                f"No readings found in {csv_path}"
            )

        target_rpm = 1600.0

        statistics = self.calculate_statistics(
            readings,
            target_rpm
        )

        status = self.determine_status(
            statistics
        )

        return statistics, status


if __name__ == "__main__":
    verification = RPMVerification()

    results_folder = (
        Path(__file__).resolve().parents[1]
        / "results"
    )

    scenario_files = [
        "normal_rpm.csv",
        "rpm_drift_rpm.csv",
        "high_deviation_rpm.csv",
        "low_deviation_rpm.csv",
        "noisy_sensor_rpm.csv"
    ]

    print()
    print("=" * 70)
    print("AUTOMATIC RPM VERIFICATION")
    print("=" * 70)

    print(
        f"{'Scenario':20}"
        f"{'Max Dev.':>12}"
        f"{'Std. Dev.':>12}"
        f"{'Status':>12}"
    )

    print("-" * 70)

    for filename in scenario_files:
        file_path = results_folder / filename

        statistics, status = verification.verify_file(
            file_path
        )

        scenario_name = filename.replace(
            "_rpm.csv",
            ""
        )

        print(
            f"{scenario_name:20}"
            f"{statistics['maximum_deviation']:>12.2f}"
            f"{statistics['standard_deviation']:>12.2f}"
            f"{status:>12}"
        )

    print("=" * 70)
    print()
    print("Project verification thresholds:")
    print("PASS    : Maximum deviation <= 5 RPM")
    print("WARNING : Maximum deviation <= 10 RPM")
    print("FAIL    : Maximum deviation > 10 RPM")
    print()
    print("These are project-defined engineering")
    print("test thresholds, not manufacturer limits.")
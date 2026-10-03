import csv
from pathlib import Path


class ProcessVerifier:
    def __init__(
        self,
        rpm_pass_limit=5.0,
        rpm_warning_limit=10.0,
        temperature_pass_limit=0.2,
        temperature_warning_limit=0.5
    ):
        self.rpm_pass_limit = rpm_pass_limit
        self.rpm_warning_limit = rpm_warning_limit
        self.temperature_pass_limit = temperature_pass_limit
        self.temperature_warning_limit = temperature_warning_limit

    @staticmethod
    def load_deviations(csv_path, deviation_column):
        path = Path(csv_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {path}"
            )

        deviations = []

        with path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                deviations.append(
                    float(row[deviation_column])
                )

        if not deviations:
            raise ValueError(
                f"No readings found in {path}"
            )

        return deviations

    def verify_rpm(self, csv_path):
        deviations = self.load_deviations(
            csv_path,
            "deviation_rpm"
        )

        maximum_deviation = max(
            abs(value)
            for value in deviations
        )

        if maximum_deviation <= self.rpm_pass_limit:
            status = "PASS"

        elif maximum_deviation <= self.rpm_warning_limit:
            status = "WARNING"

        else:
            status = "FAIL"

        return {
            "maximum_deviation": maximum_deviation,
            "status": status
        }

    def verify_temperature(self, csv_path):
        deviations = self.load_deviations(
            csv_path,
            "deviation_c"
        )

        maximum_deviation = max(
            abs(value)
            for value in deviations
        )

        if maximum_deviation <= self.temperature_pass_limit:
            status = "PASS"

        elif maximum_deviation <= self.temperature_warning_limit:
            status = "WARNING"

        else:
            status = "FAIL"

        return {
            "maximum_deviation": maximum_deviation,
            "status": status
        }

    @staticmethod
    def combine_statuses(
        rpm_status,
        temperature_status
    ):
        statuses = [
            rpm_status,
            temperature_status
        ]

        if "FAIL" in statuses:
            return "FAIL"

        if "WARNING" in statuses:
            return "WARNING"

        return "PASS"


if __name__ == "__main__":
    results_folder = (
        Path(__file__).resolve().parents[1]
        / "results"
    )

    verifier = ProcessVerifier()

    scenarios = [
        (
            "NORMAL",
            "normal_rpm.csv",
            "normal_temperature.csv"
        ),
        (
            "RPM DRIFT",
            "rpm_drift_rpm.csv",
            "normal_temperature.csv"
        ),
        (
            "HIGH RPM DEVIATION",
            "high_deviation_rpm.csv",
            "normal_temperature.csv"
        ),
        (
            "LOW RPM DEVIATION",
            "low_deviation_rpm.csv",
            "normal_temperature.csv"
        ),
        (
            "NOISY RPM SENSOR",
            "noisy_sensor_rpm.csv",
            "normal_temperature.csv"
        ),
        (
            "TEMPERATURE DRIFT",
            "normal_rpm.csv",
            "temperature_drift_temperature.csv"
        ),
        (
            "HIGH TEMPERATURE",
            "normal_rpm.csv",
            "high_temperature_temperature.csv"
        ),
        (
            "LOW TEMPERATURE",
            "normal_rpm.csv",
            "low_temperature_temperature.csv"
        ),
        (
            "NOISY TEMPERATURE SENSOR",
            "normal_rpm.csv",
            "noisy_sensor_temperature.csv"
        )
    ]

    print()
    print("=" * 95)
    print("COMBINED RPM + TEMPERATURE PROCESS VERIFICATION")
    print("=" * 95)

    print(
        f"{'Scenario':30}"
        f"{'RPM':12}"
        f"{'Temperature':15}"
        f"{'Overall':12}"
    )

    print("-" * 95)

    for (
        scenario_name,
        rpm_file,
        temperature_file
    ) in scenarios:

        rpm_result = verifier.verify_rpm(
            results_folder / rpm_file
        )

        temperature_result = (
            verifier.verify_temperature(
                results_folder / temperature_file
            )
        )

        overall_status = (
            verifier.combine_statuses(
                rpm_result["status"],
                temperature_result["status"]
            )
        )

        print(
            f"{scenario_name:30}"
            f"{rpm_result['status']:12}"
            f"{temperature_result['status']:15}"
            f"{overall_status:12}"
        )

    print("=" * 95)

    print()
    print("RPM thresholds:")
    print("PASS    : Maximum deviation <= 5 RPM")
    print("WARNING : Maximum deviation <= 10 RPM")
    print("FAIL    : Maximum deviation > 10 RPM")

    print()
    print("Temperature thresholds:")
    print("PASS    : Maximum deviation <= 0.2 °C")
    print("WARNING : Maximum deviation <= 0.5 °C")
    print("FAIL    : Maximum deviation > 0.5 °C")

    print()
    print(
        "Combined rule:"
    )
    print(
        "Any FAIL -> Overall FAIL"
    )
    print(
        "No FAIL + any WARNING -> Overall WARNING"
    )
    print(
        "Both PASS -> Overall PASS"
    )

    print()
    print(
        "All thresholds are project-defined engineering"
    )
    print(
        "test thresholds, not manufacturer limits."
    )
import csv
import random
from datetime import datetime
from pathlib import Path


class TemperatureScenarioSimulator:
    def __init__(
        self,
        target_temperature=37.0,
        duration_seconds=10,
        sample_interval=0.5,
        seed=42
    ):
        self.target_temperature = target_temperature
        self.duration_seconds = duration_seconds
        self.sample_interval = sample_interval
        self.random = random.Random(seed)

    def generate_scenario(self, scenario):
        readings = []

        total_samples = int(
            self.duration_seconds / self.sample_interval
        ) + 1

        run_id = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        for sample_number in range(total_samples):
            elapsed = (
                sample_number
                * self.sample_interval
            )

            if scenario == "normal":
                noise = self.random.gauss(
                    0,
                    0.08
                )

                measured = (
                    self.target_temperature
                    + noise
                )

            elif scenario == "temperature_drift":
                drift = (
                    sample_number
                    / (total_samples - 1)
                ) * 0.8

                noise = self.random.gauss(
                    0,
                    0.03
                )

                measured = (
                    self.target_temperature
                    + drift
                    + noise
                )

            elif scenario == "high_temperature":
                noise = self.random.gauss(
                    0,
                    0.04
                )

                measured = (
                    self.target_temperature
                    + 0.5
                    + noise
                )

            elif scenario == "low_temperature":
                noise = self.random.gauss(
                    0,
                    0.04
                )

                measured = (
                    self.target_temperature
                    - 0.5
                    + noise
                )

            elif scenario == "noisy_sensor":
                noise = self.random.gauss(
                    0,
                    0.35
                )

                measured = (
                    self.target_temperature
                    + noise
                )

            else:
                raise ValueError(
                    f"Unknown scenario: {scenario}"
                )

            deviation = (
                measured
                - self.target_temperature
            )

            readings.append({
                "run_id": run_id,
                "scenario": scenario,
                "timestamp": datetime.now().isoformat(
                    timespec="milliseconds"
                ),
                "elapsed_seconds": round(
                    elapsed,
                    2
                ),
                "target_temperature_c":
                    self.target_temperature,
                "measured_temperature_c":
                    round(measured, 3),
                "deviation_c":
                    round(deviation, 3)
            })

        return readings

    @staticmethod
    def save_csv(
        readings,
        output_path
    ):
        path = Path(output_path)
        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with path.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=readings[0].keys()
            )

            writer.writeheader()
            writer.writerows(readings)


if __name__ == "__main__":
    simulator = (
        TemperatureScenarioSimulator()
    )

    scenarios = [
        "normal",
        "temperature_drift",
        "high_temperature",
        "low_temperature",
        "noisy_sensor"
    ]

    results_folder = (
        Path(__file__).resolve().parents[1]
        / "results"
    )

    print()
    print("=" * 65)
    print("TEMPERATURE SCENARIO SIMULATION")
    print("=" * 65)

    for scenario in scenarios:
        data = simulator.generate_scenario(
            scenario
        )

        output_file = (
            results_folder
            / f"{scenario}_temperature.csv"
        )

        simulator.save_csv(
            data,
            output_file
        )

        print(
            f"{scenario.upper():25}"
            f"-> {len(data)} samples -> "
            f"{output_file.name}"
        )

    print("=" * 65)
    print(
        "All temperature scenarios generated successfully."
    )
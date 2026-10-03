import csv
import random
from datetime import datetime
from pathlib import Path


class ScenarioSimulator:
    def __init__(self, target_rpm=1600, duration_seconds=10, sample_interval=0.5):
        self.target_rpm = target_rpm
        self.duration_seconds = duration_seconds
        self.sample_interval = sample_interval

    def generate(self, scenario, seed=42):
        rng = random.Random(seed)
        readings = []

        total_samples = int(
            self.duration_seconds / self.sample_interval
        ) + 1

        run_id = (
            f"{scenario.upper()}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )

        for sample_number in range(total_samples):
            elapsed = sample_number * self.sample_interval

            if scenario == "normal":
                noise = rng.gauss(0, 3)
                measured_rpm = self.target_rpm + noise

            elif scenario == "rpm_drift":
                drift = elapsed * 1.5
                noise = rng.gauss(0, 1.5)
                measured_rpm = self.target_rpm + drift + noise

            elif scenario == "high_deviation":
                noise = rng.gauss(0, 3)
                measured_rpm = self.target_rpm + 12 + noise

            elif scenario == "low_deviation":
                noise = rng.gauss(0, 3)
                measured_rpm = self.target_rpm - 12 + noise

            elif scenario == "noisy_sensor":
                noise = rng.gauss(0, 15)
                measured_rpm = self.target_rpm + noise

            else:
                raise ValueError(
                    f"Unknown scenario: {scenario}"
                )

            measured_rpm = max(0, measured_rpm)

            readings.append({
                "run_id": run_id,
                "scenario": scenario,
                "timestamp": datetime.now().isoformat(
                    timespec="milliseconds"
                ),
                "elapsed_seconds": round(elapsed, 2),
                "target_rpm": self.target_rpm,
                "measured_rpm": round(measured_rpm, 2),
                "deviation_rpm": round(
                    measured_rpm - self.target_rpm,
                    2
                )
            })

        return readings

    @staticmethod
    def save_csv(readings, output_path):
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

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

        return path


if __name__ == "__main__":
    simulator = ScenarioSimulator()

    scenarios = [
        "normal",
        "rpm_drift",
        "high_deviation",
        "low_deviation",
        "noisy_sensor"
    ]

    results_folder = (
        Path(__file__).resolve().parents[1]
        / "results"
    )

    print("=" * 60)
    print("RPM SCENARIO SIMULATION")
    print("=" * 60)

    for index, scenario in enumerate(scenarios):
        readings = simulator.generate(
            scenario,
            seed=42 + index
        )

        output_file = (
            results_folder
            / f"{scenario}_rpm.csv"
        )

        simulator.save_csv(
            readings,
            output_file
        )

        print(
            f"{scenario.upper():20} "
            f"-> {len(readings)} samples "
            f"-> {output_file.name}"
        )

    print("=" * 60)
    print("All scenarios generated successfully.")
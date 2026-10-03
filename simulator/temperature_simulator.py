import csv
import random
import time
from datetime import datetime
from pathlib import Path


class TemperatureSimulator:
    def __init__(
        self,
        target_temperature=37.0,
        duration_seconds=10,
        sample_interval=0.5,
        noise_celsius=0.08,
        seed=None
    ):
        self.target_temperature = target_temperature
        self.duration_seconds = duration_seconds
        self.sample_interval = sample_interval
        self.noise_celsius = noise_celsius
        self.random = random.Random(seed)

    def generate_readings(self):
        readings = []

        start_time = time.time()

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

            noise = self.random.gauss(
                0,
                self.noise_celsius
            )

            measured_temperature = (
                self.target_temperature
                + noise
            )

            readings.append({
                "run_id": run_id,
                "timestamp": datetime.now().isoformat(
                    timespec="milliseconds"
                ),
                "elapsed_seconds": round(
                    elapsed,
                    2
                ),
                "target_temperature_c": (
                    self.target_temperature
                ),
                "measured_temperature_c": round(
                    measured_temperature,
                    3
                ),
                "deviation_c": round(
                    measured_temperature
                    - self.target_temperature,
                    3
                )
            })

            remaining = (
                start_time
                + elapsed
                - time.time()
            )

            if remaining > 0:
                time.sleep(remaining)

        return readings

    @staticmethod
    def save_csv(readings, output_path):
        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not readings:
            raise ValueError(
                "No temperature readings available."
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

        return path


if __name__ == "__main__":
    simulator = TemperatureSimulator(
        target_temperature=37.0,
        duration_seconds=10,
        sample_interval=0.5,
        noise_celsius=0.08,
        seed=42
    )

    data = simulator.generate_readings()

    output_file = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "sample_temperature.csv"
    )

    saved_path = simulator.save_csv(
        data,
        output_file
    )

    print(
        f"Samples generated: {len(data)}"
    )

    print(
        f"Target temperature: "
        f"{simulator.target_temperature:.2f} °C"
    )

    print(
        f"CSV saved to: {saved_path}"
    )

    print("First five readings:")

    for reading in data[:5]:
        print(reading)
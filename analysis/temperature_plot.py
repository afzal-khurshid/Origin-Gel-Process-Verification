import csv
from pathlib import Path

import matplotlib.pyplot as plt


csv_file = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "sample_temperature.csv"
)

elapsed_seconds = []
target_temperature = []
measured_temperature = []

with csv_file.open(
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        elapsed_seconds.append(
            float(row["elapsed_seconds"])
        )

        target_temperature.append(
            float(row["target_temperature_c"])
        )

        measured_temperature.append(
            float(row["measured_temperature_c"])
        )


plt.figure(figsize=(10, 5))

plt.plot(
    elapsed_seconds,
    target_temperature,
    label="Target Temperature"
)

plt.plot(
    elapsed_seconds,
    measured_temperature,
    marker="o",
    label="Measured Temperature"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Incubation Temperature Stability")

plt.grid(True)
plt.legend()

output_file = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "temperature_stability_plot.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Graph saved to: {output_file}")
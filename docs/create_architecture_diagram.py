import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 9))

ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

def box(x, y, w, h, title, subtitle=""):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.04,rounding_size=0.15",
        linewidth=1.8,
        edgecolor="black",
        facecolor="white"
    )
    ax.add_patch(patch)

    ax.text(
        x + w / 2,
        y + h * 0.62,
        title,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold"
    )

    if subtitle:
        ax.text(
            x + w / 2,
            y + h * 0.32,
            subtitle,
            ha="center",
            va="center",
            fontsize=9
        )

def arrow(x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="->",
            mutation_scale=18,
            linewidth=1.5
        )
    )

ax.text(
    7,
    9.55,
    "Origin Gel Process Verification",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

ax.text(
    7,
    9.15,
    "RPM & Temperature Integrity Verification Prototype",
    ha="center",
    va="center",
    fontsize=11
)

box(
    1,
    7.5,
    4,
    1.0,
    "RPM Data Simulation",
    "Normal / Drift / Deviation / Noise"
)

box(
    9,
    7.5,
    4,
    1.0,
    "Temperature Data Simulation",
    "Normal / Drift / High / Low / Noise"
)

box(
    1,
    5.7,
    4,
    1.0,
    "RPM Analysis",
    "Mean / Std Dev / Maximum Deviation"
)

box(
    9,
    5.7,
    4,
    1.0,
    "Temperature Analysis",
    "Mean / Std Dev / Maximum Deviation"
)

box(
    1,
    3.9,
    4,
    1.0,
    "RPM Verification",
    "PASS / WARNING / FAIL"
)

box(
    9,
    3.9,
    4,
    1.0,
    "Temperature Verification",
    "PASS / WARNING / FAIL"
)

box(
    4.5,
    2.1,
    5,
    1.0,
    "Combined Process Verification",
    "RPM + Temperature → Overall Status"
)

box(
    4.5,
    0.4,
    5,
    1.0,
    "PyQt6 Dashboard",
    "Targets / Deviations / Process Status"
)

arrow(3, 7.5, 3, 6.7)
arrow(11, 7.5, 11, 6.7)

arrow(3, 5.7, 3, 4.9)
arrow(11, 5.7, 11, 4.9)

arrow(5, 4.4, 6.0, 3.1)
arrow(9, 4.4, 8.0, 3.1)

arrow(7, 2.1, 7, 1.4)

ax.text(
    7,
    8.55,
    "Simulation Layer",
    ha="center",
    va="center",
    fontsize=10,
    fontstyle="italic"
)

ax.text(
    7,
    6.75,
    "Analysis Layer",
    ha="center",
    va="center",
    fontsize=10,
    fontstyle="italic"
)

ax.text(
    7,
    4.95,
    "Verification Layer",
    ha="center",
    va="center",
    fontsize=10,
    fontstyle="italic"
)

ax.text(
    7,
    3.35,
    "Decision Layer",
    ha="center",
    va="center",
    fontsize=10,
    fontstyle="italic"
)

ax.text(
    7,
    0.05,
    "Prototype software architecture — not a validated medical-device control system",
    ha="center",
    va="bottom",
    fontsize=8
)

plt.tight_layout()

plt.savefig(
    "docs/system_architecture.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("System architecture diagram created successfully.")
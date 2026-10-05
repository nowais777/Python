import matplotlib.pyplot as plt

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

production = [1200, 1350, 1280, 1500, 1600, 1550, 1700]

defects = [35, 42, 30, 55, 48, 60, 45]

hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
temperature = [65, 68, 72, 75, 79, 82, 85, 81, 76]


# ==========================================
# Chart 1 — Production Trend
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    days,
    production,
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=7,
    label="Production"
)

plt.title("Weekly Production Trend", fontsize=16)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Production Units", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()


# ==========================================
# Chart 2 — Defect Analysis
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    days,
    defects,
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=7,
    label="Defective Products"
)

plt.title("Weekly Defect Analysis", fontsize=16)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Defective Products", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()


# ==========================================
# Chart 3 — Machine Temperature
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    hours,
    temperature,
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=7,
    label="Temperature"
)

# Recommended temperature limit
plt.axhline(
    y=80,
    linestyle="--",
    linewidth=2,
    label="Recommended Limit: 80°C"
)

plt.title("Machine Temperature Analysis", fontsize=16)
plt.xlabel("Working Hour", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()
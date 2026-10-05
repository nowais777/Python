import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

machine_speed = [40, 45, 48, 52, 55, 58, 60, 59, 55, 50]
temperature = [60, 62, 65, 68, 72, 76, 80, 83, 81, 78]

# Create figure
fig, ax1 = plt.subplots(figsize=(10, 6))

# Machine speed
ax1.plot(
    time,
    machine_speed,
    marker='o',
    linestyle='-',
    linewidth=2,
    label="Machine Speed"
)

ax1.set_xlabel("Time")
ax1.set_ylabel("Machine Speed")
ax1.tick_params(axis='both')

# Temperature on second Y-axis
ax2 = ax1.twinx()

ax2.plot(
    time,
    temperature,
    marker='s',
    linestyle='--',
    linewidth=2,
    label="Temperature"
)

ax2.set_ylabel("Temperature (°C)")

# Title and grid
plt.title("Machine Speed and Temperature Monitoring")

ax1.grid(True, linestyle='--', alpha=0.6)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.tight_layout()
plt.show()
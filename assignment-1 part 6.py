import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
production = [1200, 1350, 1280, 1500, 1600, 1550, 1700]

# Set figure size
plt.figure(figsize=(10, 6))

# Create professional line plot
plt.plot(
    days,
    production,
    marker='o',
    linestyle='-',
    linewidth=2,
    markersize=7,
    label="Production"
)

# Add labels and title
plt.xlabel("Day", fontsize=12)
plt.ylabel("Production Units", fontsize=12)
plt.title("Weekly Production Performance", fontsize=16)

# Improve tick labels
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Display graph
plt.show()
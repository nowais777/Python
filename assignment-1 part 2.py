import matplotlib.pyplot as plt

hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
temperature = [65, 68, 72, 75, 79, 82, 85, 81, 76]

plt.plot(hours, temperature, marker='o', linestyle='-', linewidth=2)

plt.xlabel("Working Hours")
plt.ylabel("Temperature (°C)")
plt.title("Machine Temperature Throughout the Working Day")

plt.grid(True)

plt.show()
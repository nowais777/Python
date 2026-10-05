import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
production = [1200, 1350, 1280, 1500, 1600, 1550, 1700]

plt.plot(days, production, marker='o', linestyle='-', linewidth=2)

plt.xlabel("Days")
plt.ylabel("Production Units")
plt.title("Weekly Production Trend")

plt.grid(True)

plt.show()
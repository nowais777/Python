import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
production = [1000, 1200, 1150, 1400, 1350]

plt.plot(days, production)
plt.title("Weekly Production")
plt.xlabel("Days")
plt.ylabel("Production")
plt.show()
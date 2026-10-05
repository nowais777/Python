import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
total_products = [1200, 1350, 1280, 1500, 1600, 1550, 1700]
defective_products = [35, 42, 30, 55, 48, 60, 45]

plt.plot(days, total_products, marker='o', linestyle='-', linewidth=2,
         label="Total Production")

plt.plot(days, defective_products, marker='s', linestyle='--', linewidth=2,
         label="Defective Products")

plt.xlabel("Days")
plt.ylabel("Number of Products")
plt.title("Total Production vs Defective Products")

plt.legend()
plt.grid(True)

plt.show()
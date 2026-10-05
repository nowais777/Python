import matplotlib.pyplot as plt

machines = ["Machine A", "Machine B", "Machine C"]
production = [8500, 9200, 7800]

# Create bar chart
plt.bar(machines, production)

plt.xlabel("Machines")
plt.ylabel("Production Output")
plt.title("Production Output Comparison of Machines")

plt.grid(axis="y")

plt.show()
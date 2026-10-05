import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
total_products = [1200, 1350, 1280, 1500, 1600, 1550, 1700]
defective_products = [35, 42, 30, 55, 48, 60, 45]

# Calculate defect percentage
defect_percentage = []

for i in range(len(days)):
    percentage = (defective_products[i] / total_products[i]) * 100
    defect_percentage.append(percentage)

# Create line graph
plt.plot(days, defect_percentage, marker='o', linestyle='-', linewidth=2)

plt.xlabel("Days")
plt.ylabel("Defect Percentage (%)")
plt.title("Daily Product Defect Percentage")

plt.grid(True)

plt.show()

# Display percentages
for i in range(len(days)):
    print(days[i], ":", round(defect_percentage[i], 2), "%")

# Calculate average
average = sum(defect_percentage) / len(defect_percentage)
print("Average Defect Percentage:", round(average, 2), "%")
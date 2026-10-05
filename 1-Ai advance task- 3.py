product = "LAPTOP-HP-2025"

parts = product.split("-")

print("Category:", parts[0])
print("Brand:", parts[1])
print("Year:", parts[2])

print(product.partition("-"))
print(product.rpartition("-"))

result = "|".join([parts[1], parts[0], parts[2]])
print(result)
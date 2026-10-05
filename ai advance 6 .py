student = {
    "name": "Ali",
    "age": 20,
    "city": "Islamabad",
    "course": "Artificial Intelligence",
    "marks": 85
}

print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])
print("Course:", student["course"])
print("Marks:", student["marks"])



employee = {
    "employee_id": 101,
    "name": "Ahmed",
    "department": "IT",
    "salary": 75000,
    "experience": 3
}

print("Employee ID:", employee["employee_id"])
print("Name:", employee["name"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])
print("Experience:", employee["experience"], "years")




product = {
    "name": "Laptop",
    "price": 85000,
    "category": "Electronics",
    "quantity": 10,
    "brand": "Dell"
}

print("Product Name:", product["name"])
print("Product Price:", product["price"])
print("Product Category:", product["category"])
print("Product Quantity:", product["quantity"])
print("Product Brand:", product["brand"])




car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}

# This will cause a KeyError
# print(car["color"])

# Safe way using get()
print("Color:", car.get("color"))




product = {
    "id": 101,
    "name": "Laptop",
    "price": 85000,
    "stock": 15,
    "supplier": "ABC Electronics"
}

total = product["price"] * product["stock"]

print("Product:", product["name"])
print("Price:", product["price"])
print("Available Stock:", product["stock"])
print("Supplier:", product["supplier"])
print("Total Stock Value:", total)



students = {
    1: {"name": "Ali", "marks": 85},
    2: {"name": "Ahmed", "marks": 78},
    3: {"name": "Usman", "marks": 92},
    4: {"name": "Hamza", "marks": 88},
    5: {"name": "Bilal", "marks": 75}
}

print("Third Student Name:", students[3]["name"])
print("Third Student Marks:", students[3]["marks"])
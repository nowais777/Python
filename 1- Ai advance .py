employee = "   muhammad ali khan   "

print("Original:", repr(employee))

clean = employee.strip()
print("After strip:", clean)

print("Title:", clean.title())
print("Upper:", clean.upper())
print("Lower:", clean.lower())
print("Capitalize:", clean.capitalize())
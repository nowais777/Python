email = "student123@gmail.com"

print("Starts with student:", email.startswith("student"))
print("Ends with gmail.com:", email.endswith("gmail.com"))
print("@ position:", email.find("@"))
print("@ count:", email.count("@"))

new_email = email.replace("gmail.com", "company.com")
print("New Email:", new_email)

# Basic validation
if email.find("@") > 0 and email.endswith(".com") and email.count("@") == 1:
    print("Valid Email")
else:
    print("Invalid Email")
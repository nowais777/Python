password = "Python@123"

digits = 0
uppercase = 0
lowercase = 0

for char in password:
    if char.isdigit():
        digits += 1

    if char.isupper():
        uppercase += 1

    if char.islower():
        lowercase += 1

print("Number of digits:", digits)
print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)

symbols = len(password) - digits - uppercase - lowercase

if symbols > 0:
    print("Contains symbols: Yes")
else:
    print("Contains symbols: No")

print("All lowercase:", password.islower())
print("All uppercase:", password.isupper())
print("All alphabetic:", password.isalpha())
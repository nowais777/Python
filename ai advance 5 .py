# ============================================================
# Inventory Management & Sales Analysis System
# ============================================================

# Product information
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
stock = [12, 50, 30, 8, 15]
prices = [120000, 2500, 4500, 45000, 35000]


# ============================================================
# Part 1 - Display Inventory
# ============================================================

def display_inventory():
    print("\n========== INVENTORY ==========")

    for i in range(len(products)):
        print("\nProduct:", products[i])
        print("Stock:", stock[i])
        print("Price: Rs.", prices[i])


# ============================================================
# Part 2 - Calculate Inventory Value
# ============================================================

def inventory_value():
    total_value = 0

    print("\n========== INVENTORY VALUE ==========")

    for i in range(len(products)):
        value = stock[i] * prices[i]
        total_value += value

        print(
            products[i],
            "Inventory Value: Rs.",
            value
        )

    print("\nTotal Inventory Value: Rs.", total_value)


# ============================================================
# Part 3 - Find Low Stock Products
# ============================================================

def low_stock():
    print("\n========== LOW STOCK PRODUCTS ==========")

    found = False

    for i in range(len(products)):
        if stock[i] < 10:
            print(products[i], "?", stock[i], "units")
            found = True

    if found == False:
        print("No low-stock products.")


# ============================================================
# Part 4 - Find Most Expensive Product
# ============================================================

def most_expensive():
    # Start with the first product
    highest_price = prices[0]
    expensive_product = products[0]

    for i in range(1, len(products)):
        if prices[i] > highest_price:
            highest_price = prices[i]
            expensive_product = products[i]

    print("\nMost Expensive Product:", expensive_product)
    print("Price: Rs.", highest_price)


# ============================================================
# Part 5, 6, 7, 8, 9 - Customer Purchase
# ============================================================

def customer_purchase():

    # Cart quantities
    cart = [0, 0, 0, 0, 0]

    while True:

        print("\n========== PRODUCTS ==========")

        for i in range(len(products)):
            print(i + 1, ".", products[i])

        print("0. Exit")

        try:
            product_number = int(
                input("\nEnter product number: ")
            )

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Exit purchase system
        if product_number == 0:
            break

        # Validate product number
        if product_number < 1 or product_number > len(products):
            print("Invalid product number!")
            continue

        index = product_number - 1

        try:
            quantity = int(
                input("Enter quantity: ")
            )

        except ValueError:
            print("Please enter a valid quantity.")
            continue

        # Validate quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        # Check available stock
        if quantity > stock[index]:
            print("\nInsufficient stock!")
            print("Available stock:", stock[index])
            continue

        # Add product to cart
        cart[index] += quantity

        # Update inventory
        stock[index] -= quantity

        print(
            products[index],
            "added to cart."
        )

    # ========================================================
    # Generate Customer Bill
    # ========================================================

    subtotal = 0
    total_products = 0
    total_items = 0

    print("\n====================================")
    print("             CUSTOMER BILL")
    print("====================================")
    print("Product       Quantity       Total")
    print("------------------------------------")

    for i in range(len(products)):

        if cart[i] > 0:

            item_total = cart[i] * prices[i]

            print(
                products[i].ljust(15),
                str(cart[i]).ljust(15),
                item_total
            )

            subtotal += item_total
            total_products += 1
            total_items += cart[i]

    print("------------------------------------")

    # ========================================================
    # Discount Calculation
    # ========================================================

    discount = 0

    if subtotal >= 100000:
        discount = subtotal * 0.10

    elif subtotal >= 50000:
        discount = subtotal * 0.05

    else:
        discount = 0

    final_amount = subtotal - discount

    print("Subtotal: Rs.", subtotal)
    print("Discount: Rs.", discount)
    print("Final Amount: Rs.", final_amount)

    print("====================================")

    # ========================================================
    # Sales Summary
    # ========================================================

    print("\n========== SALES SUMMARY ==========")

    print(
        "Total Products Purchased:",
        total_products
    )

    print(
        "Total Items Purchased:",
        total_items
    )

    print(
        "Total Sales: Rs.",
        subtotal
    )

    print(
        "Discount: Rs.",
        discount
    )

    print(
        "Final Revenue: Rs.",
        final_amount
    )


# ============================================================
# Part 10 - Manager Menu
# ============================================================

def manager_menu():

    while True:

        print("\n====================================")
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("====================================")

        print("1. View Inventory")
        print("2. Find Low Stock")
        print("3. Find Most Expensive Product")
        print("4. Customer Purchase")
        print("5. Inventory Value")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:

            display_inventory()

        elif choice == 2:

            low_stock()

        elif choice == 3:

            most_expensive()

        elif choice == 4:

            customer_purchase()

        elif choice == 5:

            inventory_value()

        elif choice == 0:

            print("\nThank you for using the Inventory System.")
            break

        else:

            print("Invalid choice! Please try again.")


# ============================================================
# Start Program
# ============================================================

manager_menu()
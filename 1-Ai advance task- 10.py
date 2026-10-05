name = "Ali"
product = "Laptop"
price = 85000

invoice = "Customer : {}\nProduct  : {}\nPrice    : {}".format(
    name, product, price
)

print(invoice)

data = {
    "name": name,
    "product": product,
    "price": price
}

template = "Customer : {name}\nProduct  : {product}\nPrice    : {price}"

print(template.format_map(data))
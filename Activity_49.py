Tuple-Based Product Catalogue Audit

products = [
("P101", 250, 10),
("P102", 150, 0),
("P103", 500, 3),
("P104", -50, 5),
("P105", 100, -2)
]

total_value = 0

print("--- Product Catalogue Audit ---")

for product in products:
product_id, price, quantity = product

print("\nProduct ID:", product_id)
print("Price: Rs.", price)
print("Stock:", quantity)

if price < 0 or quantity < 0:
    print("Status: Invalid product record")
else:
    value = price * quantity
    total_value += value
    print("Inventory value: Rs.", value)

    if quantity == 0:
        print("Warning: Out of stock")
    elif quantity < 5:
        print("Warning: Low stock")

print("\nTotal valid inventory value: Rs.", total_value)

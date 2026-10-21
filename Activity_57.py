Smart Canteen Order and Stock Management

menu = {
"idly": 30,
"dosa": 40,
"meals": 70,
"tea": 15
}

stock = {
"idly": 50,
"dosa": 40,
"meals": 30,
"tea": 100
}

total_sales = 0

print("Welcome to Smart Canteen!")
print("\nMenu:")
for item in menu:
print(item.title(), "- Rs.", menu[item], "| Stock:", stock[item])

while True:
item = input("\nEnter item name (or 'done' to finish): ").lower()

if item == "done":
    break

if item not in menu:
    print("Item not available.")
    continue

quantity = int(input("Enter quantity: "))

if quantity <= 0:
    print("Quantity must be positive.")
elif quantity > stock[item]:
    print("Not enough stock available.")
else:
    bill = menu[item] * quantity
    stock[item] -= quantity
    total_sales += bill

    print("Order successful!")
    print("Item:", item.title())
    print("Bill: Rs.", bill)
    print("Remaining stock:", stock[item])

print("\n--- Daily Summary ---")
print("Total sales: Rs.", total_sales)
print("Remaining stock:")
for item in stock:
print(item.title(), ":", stock[item])

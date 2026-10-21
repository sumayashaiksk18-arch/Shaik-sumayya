Water Distribution Fairness Analysis

areas = int(input("Enter number of areas: "))
days = int(input("Enter number of days: "))

if areas <= 0 or days <= 0:
print("Please enter valid numbers.")
else:
total_supplied = [0] * areas
total_demand = [0] * areas

for i in range(areas):
    print("\nArea", i + 1)

    for j in range(days):
        demand = float(input("Enter water demand: "))
        supplied = float(input("Enter water supplied: "))

        if demand < 0 or supplied < 0:
            print("Invalid values. Enter non-negative values.")
            demand = 0
            supplied = 0

        total_demand[i] += demand
        total_supplied[i] += supplied

print("\n--- Water Distribution Report ---")

for i in range(areas):
    shortage = total_demand[i] - total_supplied[i]

    if shortage < 0:
        shortage = 0

    print("\nArea", i + 1)
    print("Total demand:", total_demand[i])
    print("Total supplied:", total_supplied[i])
    print("Shortage:", shortage)

    if total_demand[i] > 0:
        percentage = total_supplied[i] / total_demand[i] * 100
        print("Demand fulfilled:", round(percentage, 2), "%")

if areas > 0:
    least = min(
        range(areas),
        key=lambda i: total_supplied[i] / total_demand[i]
        if total_demand[i] > 0 else 1
    )
    print("\nArea needing attention: Area", least + 1)

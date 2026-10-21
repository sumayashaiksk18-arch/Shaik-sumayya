Food Waste Monitoring System

days = int(input("Enter number of days to analyse: "))

if days <= 0:
print("Please enter a valid number of days.")
else:
total_prepared = 0
total_served = 0
total_leftover = 0

for i in range(1, days + 1):
    print("\nDay", i)
    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    if prepared < 0 or served < 0 or served > prepared:
        print("Invalid meal quantities. Try this day again.")
        continue

    leftover = prepared - served
    waste_percent = (leftover / prepared * 100) if prepared > 0 else 0

    print("Leftover meals:", leftover)
    print("Waste percentage:", round(waste_percent, 2), "%")

    if waste_percent > 10:
        print("Warning: Food waste is above 10%.")

    total_prepared += prepared
    total_served += served
    total_leftover += leftover

print("\n--- Summary ---")
print("Total prepared:", total_prepared)
print("Total served:", total_served)
print("Total leftover:", total_leftover)

if total_prepared > 0:
    print("Overall waste percentage:",
          round(total_leftover / total_prepared * 100, 2), "%")

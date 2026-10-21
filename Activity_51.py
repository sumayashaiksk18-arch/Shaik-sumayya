Bus Passenger Occupancy Simulation

capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))

passengers = 0

if capacity <= 0 or stops <= 0:
print("Please enter valid values.")
else:
for stop in range(1, stops + 1):
print("\nStop", stop)

    getting_off = int(input("Passengers getting off: "))
    getting_on = int(input("Passengers getting on: "))

    if getting_off < 0 or getting_on < 0:
        print("Invalid passenger count.")
        continue

    if getting_off > passengers:
        print("Error: More passengers getting off than on the bus.")
        continue

    passengers -= getting_off
    passengers += getting_on

    print("Passengers currently on bus:", passengers)

    if passengers > capacity:
        print("Warning: Bus capacity exceeded!")
    else:
        print("Available seats:", capacity - passengers)

print("\n--- Final Report ---")
print("Passengers remaining on bus:", passengers)
print("Bus capacity:", capacity)

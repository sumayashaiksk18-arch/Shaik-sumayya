Nested Loop Calendar Generator

days = int(input("Enter number of days in the month (28-31): "))
start = int(input("Enter starting weekday (1=Monday, 7=Sunday): "))

if days < 28 or days > 31 or start < 1 or start > 7:
print("Invalid input!")
else:
print("Mon Tue Wed Thu Fri Sat Sun")

day = 1
position = 1

while position < start:
    print("    ", end="")
    position += 1

for day in range(1, days + 1):
    print(f"{day:3}", end=" ")

    if (start + day - 1) % 7 == 0:
        print()

print()

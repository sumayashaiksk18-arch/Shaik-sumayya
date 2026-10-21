Library Borrowing and Fine Reconciliation

books = [
("B101", 5, 0),
("B102", 10, 3),
("B103", 7, 2),
("B104", 4, 5)
]

fine_per_day = 5
total_fine = 0

print("--- Library Fine Report ---")

for book in books:
book_id, allowed_days, late_days = book

print("\nBook ID:", book_id)
print("Allowed borrowing days:", allowed_days)
print("Days overdue:", late_days)

if late_days < 0:
    print("Invalid overdue days.")
else:
    fine = late_days * fine_per_day
    total_fine += fine
    print("Fine: Rs.", fine)

    if late_days > 0:
        print("Status: Overdue")
    else:
        print("Status: Returned on time")

print("\nTotal library fine: Rs.", total_fine)

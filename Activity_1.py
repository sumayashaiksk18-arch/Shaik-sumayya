University Scholarship Allocation

name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
income = float(input("Enter family annual income: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 90 and income <= 200000 and attendance >= 75:
print("Student:", name)
print("Result: Eligible for Scholarship")
elif marks >= 75 and income <= 300000 and attendance >= 75:
print("Student:", name)
print("Result: Partially Eligible for Scholarship")
else:
print("Student:", name)
print("Result: Not Eligible for Scholarship")

Password Policy Validation Engine

password = input("Enter a sample password: ")

errors = []

if len(password) < 8:
errors.append("Password must contain at least 8 characters.")

if not any(ch.isupper() for ch in password):
errors.append("Include at least one uppercase letter.")

if not any(ch.islower() for ch in password):
errors.append("Include at least one lowercase letter.")

if not any(ch.isdigit() for ch in password):
errors.append("Include at least one digit.")

if not any(ch in "!@#$%^&" for ch in password):
errors.append("Include at least one special character (!@#$%^&).")

if errors:
print("Password is INVALID.")
for error in errors:
print("-", error)
else:
print("Password is VALID.")

Text Compression Using Character Runs

text = input("Enter a string: ")

if text == "":
print("Please enter a non-empty string.")
else:
compressed = ""
count = 1

for i in range(1, len(text) + 1):
    if i < len(text) and text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

print("Original string:", text)
print("Compressed string:", compressed)

if len(compressed) < len(text):
    print("Compression is beneficial.")
else:
    print("Compression is not beneficial.")

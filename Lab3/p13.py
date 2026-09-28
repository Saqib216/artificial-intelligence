# Write a Python program that accepts a string and calculate the number of digits and letters.

text = input("Enter a string: ")

letters = 0
digits = 0

for char in text:
    if char.isalpha():
        letters += 1

    elif char.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)
# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence

numbers = input("Enter binary numbers: ")

numbers = numbers.split(",")

result = []

for number in numbers:
    decimal = int(number, 2)

    if decimal % 5 == 0:
        result.append(number)

print(",".join(result))
# Write a Python program to count the number Of even and Odd numbers from a series of numbers.

numbers = map(int, input("Enter numbers separated by spaces: ").split())

even_count = 0
odd_count = 0

for number in numbers:
	if number % 2 == 0:
		even_count += 1
	else:
		odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
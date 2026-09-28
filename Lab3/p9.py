# Write a Python program to get the Fibonacci series between 0 to 50.
# Note: The Fibonacci sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# Fibonacci series up to 50
first, second = 0, 1
fib_series = []

while first <= 50:
    fib_series.append(first)
    first, second = second, first + second

print("Fibonacci series up to 50:", *fib_series)

# FizzBuzz for numbers 1 to 50
print("\nFizzBuzz from 1 to 50:")
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
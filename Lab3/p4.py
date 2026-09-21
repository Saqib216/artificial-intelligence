# Write a Python program to construct the following pattern, using a nested for loop.

for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()

for row in range(4, 0, -1):
    for star in range(row):
        print("*", end="")
    print()
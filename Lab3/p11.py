# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

while True:
    line = input("Enter a line: ")

    if line == "":
        break

    print(line.lower())
# Write a Python program to check the validity of password input by users. Validation

password = input("Enter password: ")

lower = False
upper = False
digit = False
special = False

for char in password:

    if char >= 'a' and char <= 'z':
        lower = True

    elif char >= 'A' and char <= 'Z':
        upper = True

    elif char >= '0' and char <= '9':
        digit = True

    elif char == '$' or char == '#' or char == '@':
        special = True


if len(password) >= 6 and len(password) <= 16:
    if lower and upper and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")
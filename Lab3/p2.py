# Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [
# Formula: c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in
# Fahrenheit]

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ").upper()

if unit == "C":
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature:g} C is {result:g} F")
elif unit == "F":
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature:g} F is {result:g} C")
else:
    print("Invalid unit. Please enter C or F.")
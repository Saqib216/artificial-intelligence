# Write a Python program that prints all the numbers from O to 6 except 3 and 6. Note : Use 'continue' statement

for num in range(0,7):
    if num in [3,6]:
        continue
    else: 
        print(num)
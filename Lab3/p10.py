# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

array = []

for i in range(m):
    row = []

    for j in range(n):
        row.append(i * j)

    array.append(row)

print(array)
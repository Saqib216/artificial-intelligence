myList = [100, 97, 297, 93, 748, 92, 932]

n = len(myList)

for i in range(1, n):
    index = i
    curr_value = myList.pop(i)
    for j in range(i-1, -1, -1):
        if myList[j] > curr_value:
            index=j
    myList.insert(index, curr_value)

print('Sorted Array:', myList)

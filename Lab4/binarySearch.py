def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [10,20,30,40,50]
target = int(input("Enter a number: "))

index = binarySearch(arr, target)

if(index==-1):
    print("Value not found")
else:
    print(f"Your target is at {index} index")
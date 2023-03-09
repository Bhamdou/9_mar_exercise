def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Enter a number to search for in the list: "))
result = binary_search(arr, x)

if result != -1:
    print("The number", x, "was found at index", result)
else:
    print("The number", x, "was not found in the list")

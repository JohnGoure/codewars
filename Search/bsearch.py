import math

def bsearch(arr, key):
    arr = sorted(arr)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = math.floor((high + low) / 2)
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
    return -1

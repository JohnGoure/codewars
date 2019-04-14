import math

def sort(arr):
    h = 1
    while h < len(arr)/3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, len(arr)):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = math.floor(h/3)
    return arr

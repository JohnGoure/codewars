def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i < len(arr) and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i + 1
        arr[i + 1] = key
    return arr

print(insertion_sort([10, 9, 8, 7, 5]))

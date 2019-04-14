def insertion_sort(arr):
    for x in range(0, len(arr)):
        i = x
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

mock = [3, 2, 1, 7, 8, 9, 10, 6, 5, 4]
print(insertion_sort(mock))

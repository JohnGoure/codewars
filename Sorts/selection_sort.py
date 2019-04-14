def selection_sort(arr):
    for x in range(len(arr)):       
        i = x
        for y in range(i + 1, len(arr)):
            if (arr[i] > arr[y]):
                i = y
        arr[x], arr[i] = arr[i], arr[x]
    return arr

print(selection_sort([10, 9, 8, 7]))

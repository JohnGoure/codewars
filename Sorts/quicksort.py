def quicksort(arr, lo, hi):
    """Sort the collection in O(NlgN) time."""
    if lo < hi:
        pivot = _partition(arr, lo, hi)

        quicksort(arr, lo, pivot - 1)
        quicksort(arr, pivot + 1, hi)


def _partition(arr, lo, hi):
    """Place the pivot element at its correct position in the sorted array."""
    i = lo - 1
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1

def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = _partition(arr, lo, hi)

        quicksort(arr, lo, pivot - 1)
        quicksort(arr, pivot + 1, high)


def _partition(arr, lo, hi):
    raise NotImplementedError("Needs to be implemented")

from Sorts.quicksort import Quicksort


def test_sort():
    arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    Quicksort().sort(arr, 0, len(arr) - 1)
    assert arr == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

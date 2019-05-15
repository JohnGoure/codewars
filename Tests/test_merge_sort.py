from Sorts.merge_sort import mergeSort


def test_sort():
    arr = [3, 2, 1]
    mergeSort(arr)
    assert arr == [1, 2, 3]

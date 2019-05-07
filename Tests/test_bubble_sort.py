from Sorts.bubble_sort import BubbleSort

def test_sort():
    mock = BubbleSort()
    assert mock.sort([2, 3, 1]) == [1, 2, 3]
from Sorts.insertion_sort import insertion_sort


def test():
    mock = [4, 3, 2]
    assert insertion_sort(mock) == sorted(mock)


def test_empty_list():
    mock = []
    assert insertion_sort(mock) == mock


def test_single_item():
    mock = [1]
    assert insertion_sort(mock) == mock


def test_mixed_items():
    mock = [1, 'a']
    assert insertion_sort(mock) == Exception

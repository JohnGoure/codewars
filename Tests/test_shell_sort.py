import Sorts.shell_sort as ShellSort


def test_sort():
    mock = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert ShellSort.shellsort(mock) == sorted(mock)

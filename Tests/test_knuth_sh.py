from Sorts.KnuthSh import ShellSort
import random

def test():
    mock = random.sample(range(1000), 1000)
    mock_Sorted = mock.sort()
    assert ShellSort(mock) == mock_Sorted

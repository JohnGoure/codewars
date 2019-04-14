from Search.bsearch import bsearch

def test_bsearch():
        assert bsearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == 2

def test_missing_key():
        assert bsearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1

def test_bsearch_sort():
        assert bsearch([3, 2, 1], 3) == 2
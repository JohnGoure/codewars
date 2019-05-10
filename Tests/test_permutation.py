from Solutions.Permutation import permutation


def test_permutation():
    """Check if one word is a permutation of another word"""
    assert permutation("dog", "god") == True


def test_non_permutation():
    """Check if one word is not a permutation of another word"""
    assert permutation("dog", "cat") == False


def test_diff_length():
    assert permutation("howdy", "more") == False


def test_longer_permutation():
    assert permutation("Cowpoke", "powokce") == True

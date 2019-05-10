from Datastructures.Permutation import permutation


def test_permutation():
    """Check if one word is a peprmutation of another word"""
    assert permutation("dog", "god") == True

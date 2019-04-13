from ToLowerCase import CaseDestroyer
from random import Random

def test_all_upper():
    mock = CaseDestroyer()
    assert mock.toLowerCase("DOG") == "dog"

def test_random_case():
    mock = CaseDestroyer()
    word = "aBcDefgHIJKLmnOpQ"
    assert mock.toLowerCase(word) == word.lower()

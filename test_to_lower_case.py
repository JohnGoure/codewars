from ToLowerCase import CaseDestroyer
import random

def test_all_upper():
    mock = CaseDestroyer()
    assert mock.toLowerCase("DOG") == "dog"

def test_random_case():
    mock = CaseDestroyer()
    word = ""
    
    for _ in range(100):
        case = random.randint(0,1)
        randomLetter = random.choice("abcdefghijklmnopqrstuvwxyz")
        if case == 1:
            word += randomLetter.upper()
        else:
            word += randomLetter.lower()

    assert mock.toLowerCase(word) == word.lower()

def permutation(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    count = {}
    for letter in word1.lower():
        if count.get(letter) == None:
            count[letter] = 1
        else:
            count[letter] += 1

    for letter in word2.lower():
        if count.get(letter) == None:
            return False
        elif count[letter] == 0:
            return False
        else:
            count[letter] -= 1
    return True

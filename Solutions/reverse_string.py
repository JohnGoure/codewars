def reverseString(word: list):
    """Reverse a list of characters in place."""
    for x in range(len(word) // 2):
        word[x], word[-1 - x] = word[-1 - x], word[x]
    return word

word = ['a', 'c', 'b', 'q', 'z', 't']
print(reverseString(word))

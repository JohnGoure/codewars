def reverseString(characters: list):
    """Reverse a list of characters in place."""
    for x in range(len(characters) // 2):
        characters[x], characters[-1 - x] = characters[-1 - x], characters[x]
    return characters

word = ['a', 'b', 'c', 'd', 'e']
print(reverseString(word))

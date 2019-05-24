
def reverseWords(words: list):
    """Reverse a list of words in place."""
    reverseCharacters(words, 0, len(words))
    start = 0
    for x in range(len(words) + 1):
        if x == len(words) or words[x] == ' ':
            reverseCharacters(words, start, x)
            start = x + 1


def reverseCharacters(characters: list, start: int, end: int):
    count = 1
    for x in range(start, (end + start) // 2):
        characters[x], characters[end - count] = characters[end - count], characters[x]
        count += 1


message = [
            'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l'
            ]

reverseWords(message)
print(message)

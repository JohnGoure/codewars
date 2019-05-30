def decrypt(encrypted_text, n):
    evenWord = []
    oddWord = []
    for x in range(len(word) // 2 - n):
        for i in range(len(text)):
            if i % 2 != 0:
                evenWord.append(text[i])
            else:
                oddWord.append(text[i])
        text = "".join(evenWord) + "".join(oddWord)
        del evenWord[:]
        del oddWord[:]
    return text


def encrypt(text, n):
    evenWord = []
    oddWord = []
    for x in range(n):
        for i in range(len(text)):
            if i % 2 != 0:
                evenWord.append(text[i])
            else:
                oddWord.append(text[i])
        text = "".join(evenWord) + "".join(oddWord)
        del evenWord[:]
        del oddWord[:]
    return text
word = 'This is a test!'
print(len(word))

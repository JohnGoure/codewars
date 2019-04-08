def compress_word(word):
    compressed_word = ""
    count = 1
    for i in range(0, len(word) - 1):
        if word[i + 1] == word[i]:
            count += 1
        if word[i] != word[i + 1] or i + 2 == len(word):
            compressed_word += f"{word[i]}{count}"
            count = 1
    if len(compressed_word) == len(word):
        return word
    return compressed_word

test = "aaa"
print(compress_word(test))

def compress_word(word):
    compressed_word = f"{word[0]}"
    count = 1
    # loop through the letters in the word
    for i in range(1, len(word)):

        if word[i - 1] != word[i]:
            compressed_word += f"{count}{word[i]}"
            count = 0
        if i == len(word) - 1:
            compressed_word += f"{count + 1}"
        count += 1
    # If the compressed word is the same length as the
    # original word, return the original word.
    if len(compressed_word) == len(word):
        return word
    return compressed_word

test = "aaaaaabbbcdefffghjklmnopqrstuvwxyz"
print(compress_word(test))

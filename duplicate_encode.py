def duplicate_encode(word):
    newWord = ""
    list = word.lower()
    for character in list:
        if word.lower().count(character) > 1:
            newWord += ")"
        else:
            newWord += "("
    return newWord

print(duplicate_encode("RkddSRFnGy"))
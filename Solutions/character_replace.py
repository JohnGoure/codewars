def replace_character(replacement, searchletter, word):
    return f'{replacement}'.join(word.lower().split(searchletter))

test = "This is only a test."
print(replace_character('%20', 't', test))


def lowercase(sentence):
    newWord = ""
    for x in sentence:
        newWord += x.lower()
    return newWord


def string_to_list(sentence, spliter=" "):

    return sentence

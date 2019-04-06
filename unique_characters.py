def is_unique(word: str) -> bool:
    wordCount = {}
    for letter in word:
        if wordCount.__contains__(letter):
            return False
        else:
            wordCount[letter] = 1

    return True

if __name__ == "__main__":
    user_input = input(
        "Please enter a word to check if it has unique characters: "
    )
    if (is_unique(user_input)):
        print(f"{user_input} is full of unique characters.")
    else:
        print(f"{user_input} has matching characters.")

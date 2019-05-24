def autocomplete(input_, dictionary):
    suggestions = []
    input_ = ''.join(letters for letters in input_ if letters.isalpha())
    for word in dictionary:
        breakpoint()
        if len(suggestions) == 5:
            return suggestions
        if word[:len(input_)].lower() == input_.lower():
            suggestions.append(word)
    return suggestions

if __name__ == '__main__':
    dic = ["dog", "cat", "door", "damage"]
    print(autocomplete("da$", dic))

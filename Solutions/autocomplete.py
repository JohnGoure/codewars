def autocomplete(input_, dictionary):
    suggestions = []
    input_ = ''.join(letters for letters in input_ if letters.isalpha())
    n = len(input_)
    for word in dictionary:
        breakpoint()
        if len(suggestions) == 5:
            return suggestions
        if word[:n].lower() == input_.lower():
            suggestions.append(word)
    return suggestions

if __name__ == '__main__':
    dic = ["dog", "cat", "door", "damage"]
    print(autocomplete("da$", dic))

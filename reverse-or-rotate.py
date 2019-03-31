def revrot(numberstring, sz):
    if sz <= 0 or numberstring == "":
        return ""
    if sz > len(numberstring):
        return ""
    numberChunk = []
    previous = 0
    for i in range(sz,len(numberstring) + 1, sz):
        sum = 0
        for x in list(map(int, numberstring[ previous : i ])):
            sum += x * x
        if sum % 2 == 0:
            numberChunk.append(list(reversed(list(map(int, numberstring[previous:i])))))
        else:
            numberChunk.append(rotateGroup(list(map(int, numberstring[ previous : i ]))))
        previous = i
    newNumberWord = ""
    for x in numberChunk:
        for letter in x:
            newNumberWord += str(letter)    
    return newNumberWord

def rotateGroup(group):
    newGroup = group[1:]
    newGroup.append(group[0])
    return newGroup

print(revrot("1224", 2))
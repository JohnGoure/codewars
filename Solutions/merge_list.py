def merge(collection1: list, collection2: list) -> list:
    answer = []

    i = j = 0
    while i < len(collection1) and j < len(collection2):
        if collection1[i] < collection2[j]:
            answer.append(collection1[i])
            i += 1
        else:
            answer.append(collection2[j])
            j += 1

    while i < len(collection1):
        answer.append(collection1[i])
        i += 1

    while j < len(collection2):
        answer.append(collection2[j])
        j += 1

    return answer

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge(my_list, alices_list))

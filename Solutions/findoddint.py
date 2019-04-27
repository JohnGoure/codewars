def find_it(seq):
    dic = {}
    for x in seq:
        if dic.__contains__(x):
            dic[x] += 1
        else: 
            dic[x] = 1
    for key, value in dic.items():
        if value % 2 != 0:
            return key

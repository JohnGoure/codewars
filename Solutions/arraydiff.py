def array_diff(a, b):
    for num in b:
        if a.__contains__(num):
            for x in range(a.count(num)):
                a.remove(num)
            
    return a

print(array_diff([1,2,2,3], [2,3]))
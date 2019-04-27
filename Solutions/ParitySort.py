from collections import deque


def parity(Arr):
    arr = deque()
    for x in Arr:
        if x % 2 == 0:
            arr.appendleft(x)
        else:
            arr.append(x)
    return list(arr)

print(parity([1,2,3,4]))

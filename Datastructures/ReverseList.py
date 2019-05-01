from Stack import Stack


def reverseList(arr):
    stack = Stack()
    for x in arr:
        stack.push(x)
    for x in range(len(arr)):
        arr[x] = stack.pop()
    return arr

print(reverseList([1, 2, 3]))

print(reverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
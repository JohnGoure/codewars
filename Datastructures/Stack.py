class Stack:
    def __init__(self):
        self.top = -1
        self.arr = []

    def push(self, item):
        self.arr.append(item)
        self.top += 1

    def peek(self):
        return self.arr[self.top]
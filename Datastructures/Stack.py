class Stack:
    def __init__(self):
        self.top = -1
        self.arr = []

    def push(self, item):
        self.arr.append(item)
        self.top += 1

    def pop(self):
        if (self.is_Empty() is False):
            item = self.arr[self.top]
            self.top -= 1
            return item
        else:
            return 'Empty Stack'

    def peek(self):
        if (self.is_Empty() is False):
            return self.arr[self.top]
        else:
            return 'Empty Stack'

    def is_Empty(self):
        return self.top == -1

from Datastructures.Stack import Stack

class Matching:
    def __init__(self):
        self.arr = Stack()

    def match(self, delimiters):
        for x in delimiters:
            if x == '{' or x == '(' or x == '[':
                self.arr.push(x)
            elif x == '}':
                if self.arr.pop() != '{':
                    return False
            elif x == ')':
                if self.arr.pop() != '(':
                    return False
            elif x == ']':
                if self.arr.pop() != '[':
                    return False

        if self.arr.is_Empty():
            return True
        else:
            return False
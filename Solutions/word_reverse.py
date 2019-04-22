from Datastructures.Stack import Stack

class Reverse:
    def __init__(self):
        self.arr = Stack()
        self.newWord = []

    def reverse(self, word):
        for letter in word:
            self.arr.push(letter)
        for _ in range(len(word)):
            self.newWord.append(self.arr.pop())
        return ''.join(self.newWord)

 
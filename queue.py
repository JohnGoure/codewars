class Queue:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.first = None

    def queue(self, key):
        newNode = self.Node(key)
        if self.first:
            n = self.first
            while n.next is not None:
                n = n.next
            n.next = newNode
        else:
            self.first = newNode

    def dequeue(self):
        result = self.first
        self.first = self.first.next
        return result

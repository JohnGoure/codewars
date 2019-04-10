class LinkedList:
    class Node:
        def __init__(self, data):
            self.next = None
            self.data = data

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = self.Node(data)
        n = self.head

        if n is None:
            self.head = newNode
        else:
            while n.next is not None:
                n = n.next
            n.next = newNode

    def __str__(self):
        if self.head is not None:
            word = f"[{self.head}"
            n = self.head
            while n.next is not None:
                word += f", {str(n.next)}"
                n = n.next
            word += "]"
            return word
        return "[]"


newList = LinkedList()
print(newList)
newList.append(2)
newList.append(7)
print(newList)
newList.append(28)
newList.append("Dogo!!!")
print(newList)

class MyQueue:
    """A first in first out collection."""
    class _Node:
        def __init__(self, key):
            self.key = key
            self.next = None

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.first = None

    def queue(self, key):
        """Place an item in the queue."""
        if key is None:
            return "Can not enqueue None"
        newNode = self._Node(key)
        if self.first:
            n = self.first
            while n.next is not None:
                n = n.next
            n.next = newNode
        else:
            self.first = newNode

    def dequeue(self):
        """Remove an item from the queue."""
        result = self.first
        self.first = self.first.next
        return result.key

    def __str__(self):
        """Return the stored keys."""
        result = [self.first.key]
        n = self.first
        while n.next is not None:
            result.append(n.next.key)
            n = n.next
        return str(result)

class Deque():
    """A queue-like data structure that supports insertion
    and deletion at both the front and the back of the queue"""

    def __init__(self, size=10):
        """Intialize the deque with size or default size of 10"""
        self._arr = [None] * size
        self._size = 0
        self._front = 0

    def add_first(self, e):
        """Add an item to the front the deque."""
        if (self._size == len(self._arr)):
            self._resize(2 * len(self._arr))
        self._arr[(self._front - 1) % len(self._arr)] = e
        self._front -= 1
        self._size += 1

    def delete_first(self):
        """Delete the first item in the deque."""
        if (self._size < len(self._arr) / 4):
            self._resize(len(self._arr) / 2)
        temp = self.first()
        self._arr[self._front % len(self._arr)] = None
        self._size -= 1
        self._front += 1
        return temp

    def first(self):
        """Return the value of the first item in the deque."""
        return self._arr[self._front % len(self._arr)]

    def add_last(self):
        """Add an item to the end of the deque."""
    # def delete_last(self):

    # def last(self):

    def is_empty(self):
        return self._size == 0

    def _resize(self, c):
        old = self._arr

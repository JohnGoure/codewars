class Deque():
    """A queue-like data structure that supports insertion
    and deletion at both the front and the back of the queue"""
    def __init__(self, size=10):
        """Intialize the deque with size or default size of 10"""
        self._arr = [None] * size
        self._size = 0
        self._front = 0

    def add_first(self, e):
        if (self._size == len(self._arr)):
            self._resize(2 * len(self._arr))

    def _resize(self, c):
        old = self._arr

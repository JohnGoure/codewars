from Datastructures.Deque import Deque


def test_add_first():
    mockDeque = Deque()
    mockDeque.add_first(1)
    mockDeque.add_first(3)
    assert mockDeque.first() == 3

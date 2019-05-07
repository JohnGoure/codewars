from Datastructures.Deque import Deque


def test_add_first():
    mockDeque = Deque()
    mockDeque.add_first(1)
    mockDeque.add_first(3)
    assert mockDeque.first() == 3


def test_delete_first():
    mockDeque = Deque()
    mockDeque.add_first(1)
    mockDeque.add_first(7)
    mockDeque.add_first(9)
    mockDeque.delete_first()
    mockDeque.delete_first()
    assert mockDeque.first() == 1


def test_add_last():
    mockDeque = Deque()
    mockDeque.add_first(1)
    mockDeque.add_last(2)
    mockDeque.delete_first()
    assert mockDeque.first() == 2

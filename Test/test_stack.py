from Datastructures.Stack import Stack

def test_insertion():
    mock = Stack()
    mock.push(2)
    assert mock.peek() == 2

def test_pop():
    mock = Stack()
    mock.push(2)
    assert mock.pop() == 2

def test_is_empty():
    mock = Stack()
    mock.push(2)
    assert mock.is_Empty() == False

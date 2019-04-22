from Datastructures.Stack import Stack

def test_insertion():
    mock = Stack()
    mock.push(2)
    assert mock.peek() == 2

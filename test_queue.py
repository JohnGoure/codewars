from myqueue import MyQueue

def test_queue_deque():
    mock_queue = MyQueue()
    mock_queue.queue(2)
    mock_queue.queue(3)
    assert mock_queue.dequeue() == 2

def test_queue_queue():
    mock = MyQueue()
    mock.queue(2)
    assert mock.first.key == 2

def test_print_queue():
    mockResult = MyQueue()
    mockTest = [x for x in range(100)]
    for x in range(100):
        mockResult.queue(x)
    assert str(mockResult) == str(mockTest)

def test_queue_next():
    mock = MyQueue()
    mock.queue(2)
    mock.queue(3)
    assert mock.first.next.key == 3

def test_queue_node():
    mock = MyQueue()
    mock.queue(2)
    assert type(mock.first) == MyQueue._Node

def test_queue_node_next_type():
    mock = MyQueue()
    mock.queue(2)
    assert mock.first.next == None

def test_queue_bad_input():
    mock = MyQueue()
    assert mock.queue(None) == "Can not enqueue None"
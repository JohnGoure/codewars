from queue import Queue

def test_queue():
    mock_queue = Queue()
    mock_queue.queue(2)
    mock_queue.queue(3)
    assert mock_queue.dequeue().key == 2
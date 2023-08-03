import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('data1')
        assert queue.head.data == 'data1'

        queue.enqueue('data2')
        assert queue.tail.data == 'data2'

        queue.enqueue('data3')
        assert queue.tail.data == 'data3'

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        assert queue.dequeue() == 'data1'
        assert queue.dequeue() == 'data2'
        assert queue.dequeue() == 'data3'

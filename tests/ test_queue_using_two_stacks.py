import pytest
from queues.queue_using_two_stacks import QueueUsingTwoStacks


class TestQueueUsingTwoStacks:

    def test_push_and_pop(self):
        q = QueueUsingTwoStacks()
        q.push(1)
        q.push(2)
        assert q.pop() == 1
        assert q.pop() == 2

    def test_peek(self):
        q = QueueUsingTwoStacks()
        q.push(1)
        q.push(2)
        assert q.peek() == 1
        assert q.pop() == 1
        assert q.peek() == 2

    def test_empty_true(self):
        q = QueueUsingTwoStacks()
        assert q.empty() is True

    def test_empty_false(self):
        q = QueueUsingTwoStacks()
        q.push(1)
        assert q.empty() is False

    def test_pop_empty_queue(self):
        q = QueueUsingTwoStacks()
        assert q.pop() == -1

    def test_peek_empty_queue(self):
        q = QueueUsingTwoStacks()
        assert q.peek() == -1

    def test_multiple_operations(self):
        q = QueueUsingTwoStacks()
        q.push(1)
        q.push(2)
        assert q.pop() == 1

        q.push(3)
        assert q.peek() == 2
        assert q.pop() == 2
        assert q.pop() == 3
        assert q.empty() is True

    def test_interleaved_operations(self):
        q = QueueUsingTwoStacks()
        q.push(10)
        assert q.peek() == 10
        q.push(20)
        assert q.pop() == 10
        q.push(30)
        assert q.pop() == 20
        assert q.pop() == 30
        assert q.empty() is True
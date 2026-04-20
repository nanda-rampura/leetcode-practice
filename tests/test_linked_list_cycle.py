import pytest
from linked_list.linked_list_cycle import LinkedListCycleDetector, ListNode


def create_cycle_list():
    """
    3 -> 2 -> 0 -> -4
         ^__________|
    """
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    return head


def create_no_cycle_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    return head


class TestLinkedListCycleDetector:

    def test_cycle_exists(self):
        head = create_cycle_list()
        assert LinkedListCycleDetector().hasCycle(head) is True

    def test_no_cycle(self):
        head = create_no_cycle_list()
        assert LinkedListCycleDetector().hasCycle(head) is False

    def test_empty_list(self):
        assert LinkedListCycleDetector().hasCycle(None) is False

    def test_single_node(self):
        head = ListNode(1)
        assert LinkedListCycleDetector().hasCycle(head) is False

    def test_single_node_cycle(self):
        head = ListNode(1)
        head.next = head
        assert LinkedListCycleDetector().hasCycle(head) is True
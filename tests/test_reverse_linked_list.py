import pytest
from linked_list.reverse_linked_list import ReverseLinkedList, ListNode


def create_list(values):
    head = None
    prev = None
    for val in values:
        node = ListNode(val)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestReverseLinkedList:

    def test_reverse_multiple_nodes(self):
        head = create_list([1, 2, 3, 4, 5])
        result = ReverseLinkedList().reverseList(head)
        assert to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_single_node(self):
        head = create_list([1])
        result = ReverseLinkedList().reverseList(head)
        assert to_list(result) == [1]

    def test_reverse_empty(self):
        result = ReverseLinkedList().reverseList(None)
        assert result is None

    def test_reverse_two_nodes(self):
        head = create_list([1, 2])
        result = ReverseLinkedList().reverseList(head)
        assert to_list(result) == [2, 1]
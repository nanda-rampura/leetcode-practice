# tests/test_middle_of_linked_list.py

from linked_list.middle_of_linked_list import MiddleOfLinkedList, ListNode


def build_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_odd_length():
    sol = MiddleOfLinkedList()
    head = build_list([1, 2, 3, 4, 5])
    result = sol.middleNode(head)
    assert list_to_array(result) == [3, 4, 5]


def test_even_length():
    sol = MiddleOfLinkedList()
    head = build_list([1, 2, 3, 4, 5, 6])
    result = sol.middleNode(head)
    assert list_to_array(result) == [4, 5, 6]


def test_single_node():
    sol = MiddleOfLinkedList()
    head = build_list([1])
    result = sol.middleNode(head)
    assert list_to_array(result) == [1]
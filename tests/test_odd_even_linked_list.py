from linked_list.odd_even_linked_list import OddEvenLinkedList
from linked_list.middle_of_linked_list import ListNode


def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for val in values:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def test_odd_even_linked_list_odd_length():
    head = build_linked_list([1, 2, 3, 4, 5])

    result = OddEvenLinkedList().oddEvenList(head)

    assert linked_list_to_list(result) == [1, 3, 5, 2, 4]


def test_odd_even_linked_list_even_length():
    head = build_linked_list([2, 1, 3, 5, 6, 4, 7])

    result = OddEvenLinkedList().oddEvenList(head)

    assert linked_list_to_list(result) == [2, 3, 6, 7, 1, 5, 4]


def test_single_node():
    head = build_linked_list([1])

    result = OddEvenLinkedList().oddEvenList(head)

    assert linked_list_to_list(result) == [1]


def test_empty_list():
    result = OddEvenLinkedList().oddEvenList(None)

    assert result is None
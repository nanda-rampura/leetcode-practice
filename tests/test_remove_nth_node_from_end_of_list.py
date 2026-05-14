from linked_list.remove_nth_node_from_end_of_list import Solution
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode(0)
    current = dummy

    for val in values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 2, [2]),
        ([1, 2], 1, [1]),
    ],
)
def test_remove_nth_from_end(head, n, expected):
    solution = Solution()

    linked_list = build_list(head)

    result = solution.removeNthFromEnd(linked_list, n)

    assert linked_list_to_list(result) == expected
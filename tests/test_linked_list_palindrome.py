import pytest
from linked_list.linked_list_palindrome import LinkedListPalindrome, ListNode


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


@pytest.mark.parametrize("values, expected", [
    ([1, 2, 2, 1], True),
    ([1, 2, 3, 2, 1], True),
    ([1, 2], False),
    ([1], True),
    ([], True),
])
def test_is_palindrome(values, expected):
    head = build_list(values)
    sol = LinkedListPalindrome()
    assert sol.isPalindrome(head) == expected
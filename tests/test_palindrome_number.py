import pytest
from topic_math.palindrome_number import Solution


@pytest.mark.parametrize("x, expected", [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (12321, True),
    (123, False),
])
def test_palindrome_number(x, expected):
    sol = Solution()
    assert sol.isPalindrome(x) == expected
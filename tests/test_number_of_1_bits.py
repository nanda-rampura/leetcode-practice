import pytest
from bit_manipulation.number_of_1_bits import Solution


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (11, 3),          # 1011
    (128, 1),         # 10000000
    (2147483645, 30), # 1111111111111111111111111111101
])
def test_hamming_weight(n, expected):
    sol = Solution()
    assert sol.hammingWeight(n) == expected
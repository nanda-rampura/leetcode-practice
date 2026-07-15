import pytest

from arrays.squares_of_sorted_array import (
    SquaresOfSortedArray,
)


class TestSquaresOfSortedArray:

    def test_mixed_numbers(self):
        nums = [-4, -1, 0, 3, 10]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [0, 1, 9, 16, 100]

    def test_all_negative(self):
        nums = [-7, -3, -1]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [1, 9, 49]

    def test_all_positive(self):
        nums = [1, 2, 3, 4]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [1, 4, 9, 16]

    def test_single_element(self):
        nums = [-5]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [25]

    def test_duplicates(self):
        nums = [-2, -2, 0, 2, 2]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [0, 4, 4, 4, 4]

    def test_contains_zero(self):
        nums = [-1, 0, 1]

        result = SquaresOfSortedArray().sortedSquares(nums)

        assert result == [0, 1, 1]
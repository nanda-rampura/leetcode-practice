import pytest

from arrays.find_duplicate_number import FindDuplicateNumber


class TestFindDuplicateNumber:

    def test_example_1(self):
        nums = [1, 3, 4, 2, 2]

        result = FindDuplicateNumber().findDuplicate(nums)

        assert result == 2

    def test_example_2(self):
        nums = [3, 1, 3, 4, 2]

        result = FindDuplicateNumber().findDuplicate(nums)

        assert result == 3

    def test_duplicate_at_beginning(self):
        nums = [1, 1, 2, 3, 4]

        result = FindDuplicateNumber().findDuplicate(nums)

        assert result == 1

    def test_duplicate_larger_value(self):
        nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]

        result = FindDuplicateNumber().findDuplicate(nums)

        assert result == 9

    def test_minimum_size(self):
        nums = [1, 1]

        result = FindDuplicateNumber().findDuplicate(nums)

        assert result == 1
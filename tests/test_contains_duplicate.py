from arrays.contains_duplicate import ContainsDuplicate


class TestContainsDuplicate:

    def test_contains_duplicate_true(self):
        nums = [1, 2, 3, 1]

        result = ContainsDuplicate().containsDuplicate(nums)

        assert result is True

    def test_contains_duplicate_false(self):
        nums = [1, 2, 3, 4]

        result = ContainsDuplicate().containsDuplicate
from arrays.majority_element import MajorityElement


class TestMajorityElement:

    def test_example_1(self):
        nums = [3, 2, 3]
        assert MajorityElement().majorityElement(nums) == 3

    def test_example_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        assert MajorityElement().majorityElement(nums) == 2

    def test_single_element(self):
        nums = [1]
        assert MajorityElement().majorityElement(nums) == 1

    def test_all_same(self):
        nums = [4, 4, 4, 4]
        assert MajorityElement().majorityElement(nums) == 4

    def test_large_input(self):
        nums = [1] * 1000 + [2] * 499
        assert MajorityElement().majorityElement(nums) == 1
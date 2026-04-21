import pytest
from arrays.three_sum import ThreeSumSolver


class TestThreeSum:

    def test_basic_case(self):
        sol = ThreeSumSolver()
        nums = [-1, 0, 1, 2, -1, -4]
        result = sol.threeSum(nums)
        expected = [
            [-1, -1, 2],
            [-1, 0, 1]
        ]
        assert sorted(result) == sorted(expected)

    def test_no_solution(self):
        sol = ThreeSumSolver()
        assert sol.threeSum([1, 2, 3]) == []

    def test_all_zeros(self):
        sol = ThreeSumSolver()
        nums = [0, 0, 0, 0]
        assert sol.threeSum(nums) == [[0, 0, 0]]

    def test_negative_only(self):
        sol = ThreeSumSolver()
        assert sol.threeSum([-5, -4, -3, -2]) == []

    def test_mixed_duplicates(self):
        sol = ThreeSumSolver()
        nums = [-2, 0, 0, 2, 2]
        expected = [[-2, 0, 2]]
        assert sol.threeSum(nums) == expected

    def test_small_input(self):
        sol = ThreeSumSolver()
        assert sol.threeSum([0]) == []
# tests/test_combination_sum.py

from backtracking.combination_sum import CombinationSum

def normalize(result):
    return sorted([sorted(r) for r in result])

def test_basic():
    sol = CombinationSum()
    result = sol.combinationSum([2,3,6,7], 7)
    assert normalize(result) == normalize([[2,2,3],[7]])

def test_single():
    sol = CombinationSum()
    result = sol.combinationSum([2], 1)
    assert result == []
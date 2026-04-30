# tests/test_subsets.py

from backtracking.subsets import Subsets

def normalize(result):
    return sorted([sorted(r) for r in result])

def test_basic():
    sol = Subsets()
    result = sol.subsets([1,2,3])
    assert normalize(result) == normalize([
        [], [1], [2], [3],
        [1,2], [1,3], [2,3],
        [1,2,3]
    ])

def test_empty():
    sol = Subsets()
    assert sol.subsets([]) == [[]]
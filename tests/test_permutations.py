# tests/test_permutations.py

from backtracking.permutations import Permutations

def normalize(result):
    return sorted(result)

def test_basic():
    sol = Permutations()
    result = sol.permute([1,2,3])
    assert normalize(result) == normalize([
        [1,2,3],[1,3,2],
        [2,1,3],[2,3,1],
        [3,1,2],[3,2,1]
    ])

def test_single():
    sol = Permutations()
    assert sol.permute([1]) == [[1]]
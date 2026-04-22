import pytest
from graphs.rotting_oranges import RottingOranges


class TestRottingOranges:

    def test_example_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        assert RottingOranges().orangesRotting(grid) == 4

    def test_example_2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        assert RottingOranges().orangesRotting(grid) == -1

    def test_no_fresh(self):
        grid = [[0,2]]
        assert RottingOranges().orangesRotting(grid) == 0

    def test_all_fresh_impossible(self):
        grid = [[1,1,1]]
        assert RottingOranges().orangesRotting(grid) == -1

    def test_single_cell(self):
        grid = [[2]]
        assert RottingOranges().orangesRotting(grid) == 0
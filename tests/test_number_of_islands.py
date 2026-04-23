from graphs.number_of_islands import NumIslands

def test_islands_basic():
    grid = [
        ["1","1","0","0"],
        ["1","1","0","0"],
        ["0","0","1","0"],
        ["0","0","0","1"]
    ]
    assert NumIslands().numIslands(grid) == 3


def test_single_island():
    grid = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    assert NumIslands().numIslands(grid) == 1


def test_no_island():
    grid = [
        ["0","0"],
        ["0","0"]
    ]
    assert NumIslands().numIslands(grid) == 0
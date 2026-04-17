import pytest
from graphs.flood_fill import Flood_Fill   # adjust folder if needed


def test_flood_fill_basic():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2

    result = Flood_Fill().floodFill(image, sr, sc, color)

    assert result == [[2,2,2],[2,2,0],[2,0,1]]


def test_flood_fill_no_change():
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    color = 0

    result = Flood_Fill().floodFill(image, sr, sc, color)

    assert result == [[0,0,0],[0,0,0]]


def test_flood_fill_single_cell():
    image = [[1]]
    sr = 0
    sc = 0
    color = 2

    result = Flood_Fill().floodFill(image, sr, sc, color)

    assert result == [[2]]


def test_flood_fill_edge_case():
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    color = 1

    result = Flood_Fill().floodFill(image, sr, sc, color)

    assert result == [[0,0,0],[0,1,1]]
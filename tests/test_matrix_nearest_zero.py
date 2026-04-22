import pytest
from graphs.matrix_nearest_zero import MatrixNearestZero


class TestMatrixNearestZero:

    def test_example_1(self):
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        expected = [[0,0,0],[0,1,0],[0,0,0]]

        assert MatrixNearestZero().updateMatrix(mat) == expected


    def test_example_2(self):
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        expected = [[0,0,0],[0,1,0],[1,2,1]]

        assert MatrixNearestZero().updateMatrix(mat) == expected


    def test_single_cell(self):
        mat = [[0]]
        expected = [[0]]

        assert MatrixNearestZero().updateMatrix(mat) == expected


    def test_line(self):
        mat = [[1,0,1,1,0]]
        expected = [[1,0,1,1,0]]

        assert MatrixNearestZero().updateMatrix(mat) == expected
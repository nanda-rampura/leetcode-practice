from backtracking.word_search import WordSearch


class TestWordSearch:

    def test_example_true(self):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCCED"

        assert WordSearch().exist(board, word) is True

    def test_example_false(self):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCB"

        assert WordSearch().exist(board, word) is False

    def test_single_cell_true(self):
        board = [["A"]]
        word = "A"

        assert WordSearch().exist(board, word) is True

    def test_single_cell_false(self):
        board = [["A"]]
        word = "B"

        assert WordSearch().exist(board, word) is False
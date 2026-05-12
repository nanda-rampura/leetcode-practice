from backtracking.letter_combinations_phone_number import LetterCombinationsPhoneNumber


class TestLetterCombinationsPhoneNumber:

    def test_example_1(self):
        digits = "23"

        result = LetterCombinationsPhoneNumber().letterCombinations(digits)

        assert sorted(result) == sorted([
            "ad","ae","af",
            "bd","be","bf",
            "cd","ce","cf"
        ])

    def test_empty_input(self):
        digits = ""

        result = LetterCombinationsPhoneNumber().letterCombinations(digits)

        assert result == []

    def test_single_digit(self):
        digits = "2"

        result = LetterCombinationsPhoneNumber().letterCombinations(digits)

        assert sorted(result) == ["a","b","c"]
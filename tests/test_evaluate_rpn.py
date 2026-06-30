from arrays.evaluate_reverse_polish_notation import EvaluateReversePolishNotation


def test_basic_addition():
    assert EvaluateReversePolishNotation().evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_basic_division():
    assert EvaluateReversePolishNotation().evalRPN(["4", "13", "5", "/", "+"]) == 6


def test_negative_numbers():
    assert EvaluateReversePolishNotation().evalRPN(["4", "-2", "/", "2", "*"]) == -4


def test_single_number():
    assert EvaluateReversePolishNotation().evalRPN(["5"]) == 5
from strings.backspace_string_compare import BackspaceStringCompare


def test_basic_true_case():
    solver = BackspaceStringCompare()

    assert solver.backspaceCompare("ab#c", "ad#c") is True


def test_basic_false_case():
    solver = BackspaceStringCompare()

    assert solver.backspaceCompare("a#c", "b") is False


def test_multiple_backspaces():
    solver = BackspaceStringCompare()

    assert solver.backspaceCompare("ab##", "c#d#") is True


def test_extra_backspaces():
    solver = BackspaceStringCompare()

    assert solver.backspaceCompare("###a", "a") is True


def test_empty_strings():
    solver = BackspaceStringCompare()

    assert solver.backspaceCompare("", "") is True
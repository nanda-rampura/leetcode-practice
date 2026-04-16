from arrays.valid_anagram import ValidAnagram

def test_valid_anagram_true():
    solution = ValidAnagram()
    assert solution.isAnagram("anagram", "nagaram") is True


def test_valid_anagram_false():
    solution = ValidAnagram()
    assert solution.isAnagram("rat", "car") is False


def test_empty_strings():
    solution = ValidAnagram()
    assert solution.isAnagram("", "") is True


def test_different_lengths():
    solution = ValidAnagram()
    assert solution.isAnagram("a", "ab") is False
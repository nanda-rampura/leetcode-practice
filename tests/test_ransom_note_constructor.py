import pytest
from strings.ransom_note_constructor import RansomNoteConstructor


class TestRansomNoteConstructor:

    def test_basic_true(self):
        assert RansomNoteConstructor().canConstruct("a", "b a") is True

    def test_basic_false(self):
        assert RansomNoteConstructor().canConstruct("aa", "ab") is False

    def test_exact_match(self):
        assert RansomNoteConstructor().canConstruct("aa", "aab") is True

    def test_empty_ransom_note(self):
        assert RansomNoteConstructor().canConstruct("", "abc") is True

    def test_empty_magazine(self):
        assert RansomNoteConstructor().canConstruct("a", "") is False

    def test_repeated_characters(self):
        assert RansomNoteConstructor().canConstruct("aabb", "ab") is False

    def test_large_case(self):
        assert RansomNoteConstructor().canConstruct("abc", "aabbcc") is True
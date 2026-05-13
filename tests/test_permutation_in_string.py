from sliding_window.permutation_in_string import PermutationInString


class TestPermutationInString:

    def test_example_1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        assert PermutationInString().checkInclusion(s1, s2) is True

    def test_example_2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        assert PermutationInString().checkInclusion(s1, s2) is False

    def test_exact_match(self):
        s1 = "abc"
        s2 = "abc"
        assert PermutationInString().checkInclusion(s1, s2) is True

    def test_s1_longer_than_s2(self):
        s1 = "abcd"
        s2 = "abc"
        assert PermutationInString().checkInclusion(s1, s2) is False
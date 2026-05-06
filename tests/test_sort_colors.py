from arrays.sort_colors import SortColors


class TestSortColors:

    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        SortColors().sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_example_2(self):
        nums = [2, 0, 1]
        SortColors().sortColors(nums)
        assert nums == [0, 1, 2]

    def test_all_same(self):
        nums = [1, 1, 1]
        SortColors().sortColors(nums)
        assert nums == [1, 1, 1]

    def test_single_element(self):
        nums = [0]
        SortColors().sortColors(nums)
        assert nums == [0]

    def test_reverse_order(self):
        nums = [2, 2, 1, 1, 0, 0]
        SortColors().sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]
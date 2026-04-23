from arrays.merge_intervals import MergeIntervals

class TestMergeIntervals:

    def test_basic_merge(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        assert MergeIntervals().merge(intervals) == [[1,6],[8,10],[15,18]]

    def test_touching_intervals(self):
        intervals = [[1,4],[4,5]]
        assert MergeIntervals().merge(intervals) == [[1,5]]

    def test_reverse_order(self):
        intervals = [[4,7],[1,4]]
        assert MergeIntervals().merge(intervals) == [[1,7]]

    def test_no_overlap(self):
        intervals = [[1,2],[3,4],[5,6]]
        assert MergeIntervals().merge(intervals) == [[1,2],[3,4],[5,6]]

    def test_single_interval(self):
        intervals = [[1,10]]
        assert MergeIntervals().merge(intervals) == [[1,10]]
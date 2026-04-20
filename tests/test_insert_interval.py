from arrays.insert_interval import InsertInterval


class TestInsertInterval:

    def test_basic_insert(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]

        result = InsertInterval().insert(intervals, newInterval)

        assert result == [[1,5],[6,9]]

    def test_merge_all(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]

        result = InsertInterval().insert(intervals, newInterval)

        assert result == [[1,2],[3,10],[12,16]]

    def test_no_overlap(self):
        intervals = [[1,2],[5,6]]
        newInterval = [3,4]

        result = InsertInterval().insert(intervals, newInterval)

        assert result == [[1,2],[3,4],[5,6]]
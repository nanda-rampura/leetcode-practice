from arrays.k_closest_points import KClosestPoints


class TestKClosestPoints:

    def test_basic_case(self):
        points = [[1,3],[-2,2],[5,8],[0,1]]
        k = 2

        result = KClosestPoints().kClosest(points, k)

        assert sorted(result) == sorted([[-2,2],[0,1]])

    def test_single_point(self):
        points = [[1,1]]
        k = 1

        result = KClosestPoints().kClosest(points, k)

        assert result == [[1,1]]

    def test_all_same_distance(self):
        points = [[1,1],[-1,-1],[2,2]]
        k = 2

        result = KClosestPoints().kClosest(points, k)

        assert len(result) == 2

    def test_negative_coordinates(self):
        points = [[-2,-3],[3,4],[0,0]]
        k = 2

        result = KClosestPoints().kClosest(points, k)

        assert sorted(result) == sorted([[0,0],[-2,-3]])
from arrays.container_with_most_water import ContainerWithMostWater


class TestContainerWithMostWater:

    def test_example_1(self):
        height = [1,8,6,2,5,4,8,3,7]

        result = ContainerWithMostWater().maxArea(height)

        assert result == 49

    def test_small_array(self):
        height = [1,1]

        result = ContainerWithMostWater().maxArea(height)

        assert result == 1

    def test_monotonic_increasing(self):
        height = [1,2,3,4,5]

        result = ContainerWithMostWater().maxArea(height)

        assert result == 6
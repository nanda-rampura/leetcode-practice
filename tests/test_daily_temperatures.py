from stacks.daily_temperatures import DailyTemperatures


class TestDailyTemperatures:

    def test_example_1(self):
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        result = DailyTemperatures().dailyTemperatures(temps)
        assert result == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_example_2(self):
        temps = [30, 40, 50, 60]
        result = DailyTemperatures().dailyTemperatures(temps)
        assert result == [1, 1, 1, 0]

    def test_descending(self):
        temps = [90, 80, 70, 60]
        result = DailyTemperatures().dailyTemperatures(temps)
        assert result == [0, 0, 0, 0]

    def test_single_element(self):
        temps = [100]
        result = DailyTemperatures().dailyTemperatures(temps)
        assert result == [0]
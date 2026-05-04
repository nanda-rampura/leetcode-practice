from arrays.binary_adder import BinaryStringAdder

class TestBinaryStringAdder:

    def test_example_1(self):
        assert BinaryStringAdder.addBinary("11", "1") == "100"

    def test_example_2(self):
        assert BinaryStringAdder.addBinary("1010", "1011") == "10101"

    def test_zero(self):
        assert BinaryStringAdder.addBinary("0", "0") == "0"

    def test_unequal_lengths(self):
        assert BinaryStringAdder.addBinary("1", "1111") == "10000"

    def test_large_input(self):
        a = "1" * 500
        b = "1"
        result = BinaryStringAdder.addBinary(a, b)
        assert len(result) == 501
        assert result.startswith("1")
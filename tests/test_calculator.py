from calculator.calculator import Calculator

class TestCalculator:
    def test_add_positive(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_negative(self):
        # arrange
        a = -3
        b = -5
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -8
        assert result == expected

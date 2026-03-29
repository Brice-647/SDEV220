import unittest
from calculator import get_number, double_number


class TestCalculator(unittest.TestCase):

    def test_valid_input(self):
        """Test that valid input is converted correctly"""
        result = get_number("5")
        self.assertEqual(result, 5)

    def test_invalid_input(self):
        """Test that invalid input raises an error"""
        with self.assertRaises(ValueError):
            get_number("abc")


if __name__ == "__main__":
    unittest.main()
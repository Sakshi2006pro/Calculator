import unittest
from calculator import add, subtract, multiply, divide, format_number


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-2, 3), 1)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-3, -7), 4)

    def test_multiply(self):
        self.assertEqual(multiply(7, 8), 56)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)
        self.assertEqual(divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_format_number(self):
        self.assertEqual(format_number(5.0), "5")
        self.assertEqual(format_number(-3.0), "-3")
        self.assertEqual(format_number(3.14), "3.14")


if __name__ == "__main__":
    unittest.main()

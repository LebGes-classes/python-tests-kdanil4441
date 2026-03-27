import unittest
from math_utils import add, subtract, multiply, divide, create_data


class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-10, -15), -25)
        self.assertEqual(round(add(3.14, 2.86), 7), 6.0)
        self.assertEqual(round(add(-1.5, 1.5), 7), 0.0)
        self.assertEqual(add(1000000, 1), 1000001)
        self.assertEqual(round(add(0.0001, 0.0009), 7), 0.001)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(round(subtract(7.5, 2.5), 7), 5.0)
        self.assertEqual(round(subtract(3.14, 1.14), 7), 2.0)
        self.assertEqual(round(subtract(100, 99.9), 7), 0.1)
        self.assertEqual(subtract(-10, 5), -15)
        with self.assertRaises(TypeError):
            subtract("10", 5)
        with self.assertRaises(TypeError):
            subtract(15, "5")
        self.assertEqual(subtract(0, -5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, -1), 3)
        self.assertEqual(multiply(-13, 2), -26)
        self.assertEqual(round(multiply(-1.6, -2.5), 7), 4.0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(round(multiply(5.2, 2), 7), 10.4)
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(round(multiply(0.5, 0.5), 7), 0.25)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        self.assertEqual(round(divide(7.5, 2.5), 7), 3.0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333, places=7)
        with self.assertRaises(TypeError):
            divide("10", 2)
        with self.assertRaises(TypeError):
            divide(10, "2")
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    def test_with_create_data(self):
        a, b = create_data()
        self.assertEqual(add(a, b), 5)


if __name__ == '__main__':
    unittest.main()
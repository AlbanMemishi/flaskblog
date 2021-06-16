import unittest
import calculation


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculation.add(10, 5), 15)
        self.assertEqual(calculation.add(-1, 1), 0)
        self.assertEqual(calculation.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculation.subtract(10, 5), 5)
        self.assertEqual(calculation.subtract(-1, 1), -2)
        self.assertEqual(calculation.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculation.multiply(10, 5), 50)
        self.assertEqual(calculation.multiply(-1, 1), -1)
        self.assertEqual(calculation.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculation.divide(10, 5), 2)
        self.assertEqual(calculation.divide(-1, 1), -1)
        self.assertEqual(calculation.divide(-1, -1), 1)
        self.assertEqual(calculation.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calculation.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

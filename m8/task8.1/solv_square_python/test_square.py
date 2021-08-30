import unittest
from main import discriminant, validate_param_, roots, main


class TestDisc(unittest.TestCase):
    def test_minus(self):
        print("Correct! d=", discriminant(2,4,6))
        self.assertEqual(discriminant(2, 4, 6), -32, msg='not equal')

    def test_zero(self):
        print("Correct! d=", discriminant(16, 8, 1))
        self.assertEqual(discriminant(16, 8, 1), 0, msg='not equal')

    def test_plus(self):
        print("Correct  d=", discriminant(1, 1, -1))
        self.assertEqual(discriminant(1, 1, -1), 5, msg='not equal')

    def test_value(self):
        with self.assertRaises(ValueError) as e:
            discriminant(0, 0, 0)


class TestRoots(unittest.TestCase):
    def test_x(self):
        print("d =", discriminant(16, 8, 1))
        self.assertEqual(roots(0, 16, 8, 1), -0.25)


class TestValid(unittest.TestCase):
    def test_val(self):
        self.assertEqual((validate_param_('49')), 49)


if __name__ == '__main__':
    unittest.main()

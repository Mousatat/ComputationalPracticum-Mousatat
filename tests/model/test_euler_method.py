import unittest
import numpy as np

from model.approximations.euler_method import EulerApproximation


class TestEulerMethod(unittest.TestCase):
    def setUp(self):
        self.method = EulerApproximation(derivative_function=lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2)

    def test_case(self):
        expected = np.array([2.0, 2.5, 3.1438017, 3.9921386, 5.1422544, 6.75868])
        val = np.zeros(shape=6)
        val[0] = 2.0
        for i, x in enumerate(np.linspace(1, 1.4, 5)):
            val[i+1] = self.method(x, val[i])

        np.testing.assert_array_almost_equal(val, expected)


if __name__ == '__main__':
    unittest.main()

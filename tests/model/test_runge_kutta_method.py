import unittest
import numpy as np

from model.approximations.runge_kutta_method import RungeKuttaApproximation


class TestRungeKuttaMethod(unittest.TestCase):
    def setUp(self):
        self.method = RungeKuttaApproximation(derivative_function=lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2)

    def test_case(self):
        expected = np.array([2.0, 2.5870054, 3.4148858, 4.652771, 6.6726, 10.4830265], dtype=np.float32)
        val = np.zeros(shape=6, dtype=np.float32)
        val[0] = 2.0
        for i, x in enumerate(np.linspace(1, 1.4, 5)):
            val[i+1] = self.method(x, val[i])

        np.testing.assert_array_almost_equal(val, expected)


if __name__ == '__main__':
    unittest.main()

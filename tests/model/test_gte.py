import unittest
import numpy as np

from model.errors.gte import GlobalTruncationError
from model.exceptions.incorrect_params_error import IncorrectParamsError
from model.exceptions.incorrect_param_type_error import IncorrectParamTypeError
from model.approximations.euler_method import EulerApproximation
from model.approximations.improved_euler_method import ImprovedEulerApproximation
from model.approximations.runge_kutta_method import RungeKuttaApproximation


class TestGTE(unittest.TestCase):
    def setUp(self):
        solution_function = lambda x: (x * (1 + x ** 2 / 3)) / (1 - x ** 2 / 3)
        self.derivative_func = lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2

        self.gte = GlobalTruncationError(solution_function)

    def test_euler(self):
        expected = np.array([0., 0.087150835, 0.27158296, 0.66205996, 1.5346692, 3.741321], dtype=np.float32)
        val = self.gte(EulerApproximation(self.derivative_func), 1, 1.5, count=6)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_improved_euler(self):
        expected = np.array([0., 0.01368145, 0.04639308, 0.12658027, 0.34270477, 1.0465215], dtype=np.float32)
        val = self.gte(ImprovedEulerApproximation(self.derivative_func), x0=1.0, endpoint=1.5, count=6, y0=2.0)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_rkm(self):
        expected = np.array([0., 0.000145517, 0.0004988718, 0.0014275842, 0.004323864, 0.016975135], dtype=np.float32)
        val = self.gte(RungeKuttaApproximation(self.derivative_func), x0=1., endpoint=1.5, count=6)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_absence_params(self):
        self.assertRaises(IncorrectParamsError,
                          self.gte, EulerApproximation(self.derivative_func), 1, 1.5)

    def test_incorrect_type_step(self):
        self.assertRaises(IncorrectParamTypeError, self.gte,
                          ImprovedEulerApproximation(self.derivative_func), 1, 1.5, step='0.1')

    def test_incorrect_type_count(self):
        self.assertRaises(IncorrectParamTypeError, self.gte,
                          RungeKuttaApproximation(self.derivative_func), 1, 1.5, count=4.5)

    def test_step_and_count(self):
        self.assertRaises(IncorrectParamsError, self.gte,
                          EulerApproximation(self.derivative_func), 1, 1.5, step=.1, count=5)


if __name__ == '__main__':
    unittest.main()

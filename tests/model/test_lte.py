import unittest
import numpy as np

from model.errors.lte import LocalTruncationError
from model.exceptions.incorrect_params_error import IncorrectParamsError
from model.exceptions.incorrect_param_type_error import IncorrectParamTypeError
from model.approximations.euler_method import EulerApproximation
from model.approximations.improved_euler_method import ImprovedEulerApproximation
from model.approximations.runge_kutta_method import RungeKuttaApproximation


class TestLTE(unittest.TestCase):
    def setUp(self):
        test_func = lambda x: (x * (1 + x ** 2 / 3)) / (1 - x ** 2 / 3)
        self.derivative_func = lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2

        euler_method = EulerApproximation(self.derivative_func)
        improved_euler_method = ImprovedEulerApproximation(self.derivative_func)
        runge_kutta_method = RungeKuttaApproximation(self.derivative_func)

        self.lte = LocalTruncationError(test_func)

    def test_euler(self):
        expected = np.array([0., 0.087150835, 0.13986887, 0.2441393, 0.48296002, 1.1715976], dtype=np.float32)
        val = self.lte(EulerApproximation(self.derivative_func), 1, 1.5, count=6)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_improved_euler(self):
        expected = np.array([0., 0.01368145, 0.023602538, 0.04599498, 0.106638946, 0.32514724], dtype=np.float32)
        val = self.lte(ImprovedEulerApproximation(self.derivative_func), x0=1.0, endpoint=1.5, count=6, y0=2.0)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_rkm(self):
        expected = np.array([0., 0.000145517, 0.00025022254, 0.0005286229, 0.0014980546, 0.0067819976],
                            dtype=np.float32)
        val = self.lte(RungeKuttaApproximation(self.derivative_func), x0=1., endpoint=1.5, step=.1)

        self.assertIs(type(val), np.ndarray)
        self.assertEqual(len(val), 6)
        self.assertEqual(len(val), len(expected))
        np.testing.assert_array_almost_equal(val, expected)

    def test_absence_params(self):
        self.assertRaises(IncorrectParamsError, self.lte,
                          EulerApproximation(self.derivative_func), 1, 1.5)

    def test_incorrect_type_step(self):
        self.assertRaises(IncorrectParamTypeError, self.lte,
                          ImprovedEulerApproximation(self.derivative_func), 1, 1.5, step='0.1')

    def test_incorrect_type_count(self):
        self.assertRaises(IncorrectParamTypeError, self.lte,
                          RungeKuttaApproximation(self.derivative_func), 1, 1.5, count=4.5)

    def test_step_and_count(self):
        self.assertRaises(IncorrectParamsError, self.lte,
                          EulerApproximation(self.derivative_func), 1, 1.5, step=.1, count=5)


if __name__ == '__main__':
    unittest.main()

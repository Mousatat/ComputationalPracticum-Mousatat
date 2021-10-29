import numpy
import numpy as np

from model.approximations.euler_method import EulerApproximation
from model.approximations.improved_euler_method import ImprovedEulerApproximation
from model.approximations.runge_kutta_method import RungeKuttaApproximation
from model.errors.lte import LocalTruncationError
from model.errors.gte import GlobalTruncationError


class Model:
    """
    Represents the model in MVC pattern.
    Contains business logic and necessary calculations.
    It provides an interface to work with data.
    """
    def __init__(self):
        """ Model initialization. """
        self._const = 1
        self.__solution_function = lambda x: (x/3+1/6+np.exp(2*(x-1))*(2**(2/3)-1/2))**(3/2)
        self.__derivative_function = lambda x , y: 3 * y - x * (y ** (1/3))

        self._euler_method = EulerApproximation(self.__derivative_function)
        self._improved_euler_method = ImprovedEulerApproximation(self.__derivative_function)
        self._runge_kutta_method = RungeKuttaApproximation(self.__derivative_function)
        self._lte = LocalTruncationError(self.__solution_function)
        self._gte = GlobalTruncationError(self.__solution_function)

        self.x0 = 1
        self.y0 = 2
        self.X = 5
        self.steps = 50

        self.n0 = 10
        self.N = 100

    def change_initial_condition(self, x0: float = None, y0: float = None) -> None:
        """
        Changes initial value of a constant in the equation according to new values of x0 and y0.
        :param x0: x0 in the initial condition.
        :param y0: corresponding solution of x0 in the initial condition.
        """
        if x0 is not None:
            self.x0 = x0
        if y0 is not None:
            self.y0 = y0
        self._const = (self.y0 + self.x0**2 + 1) * np.exp(-(self.x0**2))

    def x_plane(self) -> np.ndarray:
        """
        Creates x-plane from values self.x0 to self.X with number of steps equals self.steps.
         dtype is specified because of exponential function (solution function)
         can raise OverflowError during calculation with big numbers
         (For example, exp(1234.1) will raise the exception.)
        :return: np.array of values x from self.x0 to self.X with number of steps = self.steps.
        """
        return np.linspace(self.x0, self.X, self.steps, dtype=np.float64)

    def exact(self) -> np.ndarray:
        """
        Calculates exact solution for values of x which are returned from self.x_plane() function.
        :return: np.array of values of exact solution on given array.
        """
        return self.__solution_function(self.x_plane())

    def euler_method(self) -> np.ndarray:
        """
        Calculates approximation using Euler's method.
         see self._calculate_approximation function for more details.
        :return: np.array with values of approximate values of x using Euler's method.
        """
        print(f"Euler method: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._calculate_approximation(self._euler_method)

    def improved_euler_method(self) -> np.ndarray:
        """
        Calculates approximation using Improved Euler's method.
         see self._calculate_approximation function for more details.
        :return: np.array with values of approximate values of x using Improved Euler's method.
        """
        print(f"Improved Euler method: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._calculate_approximation(self._improved_euler_method)

    def runge_kutta_method(self) -> np.ndarray:
        """
        Calculates approximation using Runge Kutta method.
         see self._calculate_approximation function for more details.
        :return: np.array with values of approximate values of x using Runge Kutta method.
        """
        print(f"Runge Kutta method: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._calculate_approximation(self._runge_kutta_method)

    def _calculate_approximation(self, method) -> np.ndarray:
        """
        Calculates approximate values of x using given approximation method.
        :param method: Approximation method for calculating approximate solution for x.
         Can be one of [EulerApproximation, ImprovedEulerApproximation, RungeKuttaApproximation].
        :return: np.array with values of approximate values of x using given method.
        """
        xs = self.x_plane()
        arr = np.zeros(shape=self.steps, dtype=np.float64)
        arr[0] = self.__solution_function(xs[0])
        step = float(xs[1] - xs[0])
        for i in range(1, self.steps):
            arr[i] = method(xs[i - 1], arr[i - 1], step)
        return arr

    def euler_lte(self):
        print(f"Euler LTE: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._lte(self._euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def improved_euler_lte(self):
        print(f"Improved Euler LTE: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._lte(self._improved_euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def runge_kutta_lte(self):
        print(f"Runge Kutta LTE: x0={self.x0}, y0={self.y0}, X={self.X}, steps={self.steps}")
        return self._lte(self._runge_kutta_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def euler_gte(self):
        return self._gte(self._euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def improved_euler_gte(self):
        return self._gte(self._improved_euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def runge_kutta_gte(self):
        return self._gte(self._runge_kutta_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def n_plane(self):
        return np.linspace(self.n0, self.N, self.N - self.n0 + 1, dtype=np.int)

    def euler_lte_errors(self):
        print(f"Euler's LTE errors: x0={self.x0}, y0={self.y0}, X={self.X}, n0={self.n0}, N={self.N}")
        return np.array([
            numpy.amax(self._lte(self._euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def improved_euler_lte_errors(self):
        print(f"Improved Euler's LTE errors: x0={self.x0}, y0={self.y0}, X={self.X}, n0={self.n0}, N={self.N}")
        return np.array([
            numpy.amax(self._lte(self._improved_euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def runge_kutta_lte_errors(self):
        print(f"Runge Kutta LTE errors: x0={self.x0}, y0={self.y0}, X={self.X}, n0={self.n0}, N={self.N}")
        return np.array([
            numpy.amax(self._lte(self._runge_kutta_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def euler_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def improved_euler_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._improved_euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def runge_kutta_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._runge_kutta_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

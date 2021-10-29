import numpy as np
from math import ceil

from model.exceptions.incorrect_param_type_error import IncorrectParamTypeError
from model.exceptions.incorrect_params_error import IncorrectParamsError


class GlobalTruncationError:
    """ Class represents global truncation error (GTE) of a function and its approximation. """

    def __init__(self, solution_function):
        """
        Initialization of the GTE.

        :param solution_function: function that represents exact solution.
         Can be one of the 3 options: "Euler's method", "Improved Euler's method", "Runge Kutta method".
        """
        self.solution_function = solution_function

    def __call__(self, approximation_method, x0, endpoint, **kwargs) -> np.ndarray:
        """
        Function calculates global truncation error (GTE) for a given range.
        Make sure to pass one of the following parameters: step, count.

        :param approximation_method: approximation method for the equation.
        :param x0: starting point for a function.
        :param endpoint: endpoint for a function.
        :param kwargs: Should include either 'step' - a step of a function,
         nor 'count' - a number of steps needed to calculate.
         It can contain solution 'y0' for the first point (x0).
        :return: numpy.array of size (1, 'count'),
         if count is not specified then size will be (1, ('endpoint' - 'start point') / 'step')
        """
        if 'step' not in kwargs and 'count' not in kwargs:
            raise IncorrectParamsError('step', 'count')
        elif 'step' in kwargs:
            if type(kwargs['step']) in [int, float]:
                steps = ceil((endpoint - x0) / kwargs['step']) + 1
            else:
                raise IncorrectParamTypeError('step', type(kwargs['step']), (int, float))
        else:
            if type(kwargs['count']) is int:
                steps = kwargs['count']
            else:
                raise IncorrectParamTypeError('count', type(kwargs['count']), int)
        if 'step' in kwargs and 'count' in kwargs and steps != kwargs['count']:
            raise IncorrectParamsError(
                message='Parameters "step", "count" should not be passed into function at the same time'
            )

        if 'y0' in kwargs and type(kwargs['y0']) in [int, float]:
            y0 = kwargs['y0']
        else:
            y0 = self.solution_function(x0)

        if 'step' not in kwargs:
            if steps <= 1:
                step = 0
            else:
                step = np.linspace(x0, endpoint, steps)[1] - x0
        else:
            step = kwargs['step']

        arr = np.zeros(shape=steps, dtype=np.float64)
        xi = x0
        y_approximate = y0
        for i, x in enumerate(np.linspace(x0, endpoint, steps)):
            if i == 0:
                continue
            y_approximate = approximation_method(xi, y_approximate, step)
            y_real = self.solution_function(x)
            arr[i] = abs(y_real - y_approximate)
            xi = x
        return arr

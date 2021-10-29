class RungeKuttaApproximation:
    """ Represents Runge Kutta approximation method to find next value of a given function. """

    def __init__(self, derivative_function):
        """
        Initialization of Runge Kutta method.

        :param derivative_function: initial function.
        """
        self.derivative_function = derivative_function

    def __call__(self, xi: [int, float], yi: [int, float], step=.1) -> float:
        """
        Runge Kutta approximation method.

        :param xi: previous value of x.
        :param yi: previous value of y.
        :param step: importance of rate of change previous value of function on a new one.
        :return: approximate next value of the function.
        """
        k1 = self.derivative_function(xi, yi)
        k2 = self.derivative_function(xi + step / 2, yi + step * k1 / 2)
        k3 = self.derivative_function(xi + step / 2, yi + step * k2 / 2)
        k4 = self.derivative_function(xi + step, yi + step * k3)
        return yi + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

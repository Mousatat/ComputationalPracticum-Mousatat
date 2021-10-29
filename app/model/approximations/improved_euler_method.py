class ImprovedEulerApproximation:
    """ Represents improved Euler's approximation method for finding next value of a given function. """

    def __init__(self, derivative_function):
        """
        Initialization of improved Euler's method.

        :param derivative_function: initial function.
        """
        self.derivative_function = derivative_function

    def __call__(self, xi: [int, float], yi: [int, float], step=.1) -> float:
        """
        Improved Euler's approximation method.

        :param xi: previous value of x.
        :param yi: previous value of y.
        :param step: importance of rate of change previous value of function on a new one.
        :return: approximate next value of the function.
        """
        return yi + step * self.derivative_function(
            xi + step / 2,
            yi + step / 2 * self.derivative_function(xi, yi)
        )

class IncorrectParamsError(Exception):
    """ Exception for incorrect parameters passed to functions. """

    def __init__(self, *args, message='You should pass to function the following params: {}'):
        """
        Attributes:
        :param expression: input expression in which the error occurred.
        :param message: explanation of the error.
        """
        self.message = message.format(args)
        super().__init__(self.message)

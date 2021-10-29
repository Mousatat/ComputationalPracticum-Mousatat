class IncorrectParamTypeError(Exception):
    def __init__(self, param, given_type, expected):
        self.message = f'Parameter "{param}" has incorrect type. Expected: {expected}, but given: {given_type}'
        super().__init__(self.message)

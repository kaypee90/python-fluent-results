"""
Custom defined exceptions
"""


class MessageNotStringError(Exception):
    """Exception raised for errors when message in not a string.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="message must be a string"):
        self.message = message
        super().__init__(self.message)


class MessageNotEmptyError(Exception):
    """Exception raised for errors when message is empty or null.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="message must not be empty!"):
        self.message = message
        super().__init__(self.message)

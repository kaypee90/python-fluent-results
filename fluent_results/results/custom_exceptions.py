"""
Custom defined exceptions
"""


class Error(Exception):
    """
    Base class for other exceptions
    """


class MessageNotStringError(Error):
    """Exception raised for errors when message in not a string.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message, *args):
        self.message = message or "message must be a string"
        self.args = args
        super().__init__(self.message)


class MessageNotEmptyError(Error):
    """Exception raised for errors when message is empty or null.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message, *args):
        self.message = message or "message must not be empty!"
        self.args = args
        super().__init__(self.message)


class BulkMessagesTypeError(Error):
    """
    Exception raised for errors when passed list of messages
    is not a list of strings.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message, *args):
        self.message = message or "messages must be a list of strings"
        self.args = args
        super().__init__(self.message)

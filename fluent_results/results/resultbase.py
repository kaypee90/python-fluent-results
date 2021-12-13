"""
Author kaypee90
"""

from abc import ABC

class ResultBase(ABC):
    """
    Base class for all results
    """
    def __init__(self, is_success, data=None, message=None):  
        self.errors = []
        self.successes = []
        self.reasons = []
        self.value = data
        self.is_success = is_success

        ResultBase.validate_message(message)

        if is_success and message:
            self.successes.append(message)

        if not is_success and message:
            self.errors.append(message)

    @property
    def is_failed(self):
        return not self.is_success

    def with_error(self, error_message):
        """
        takes in a error message and adds it to
        the list of error messages.

        params:
            error_message (str): message to be added
        returns
            ResultBase: an instance of result bbase
        """
        ResultBase.validate_message(error_message, True)
        self.errors.append(error_message)
        return self

    @staticmethod
    def validate_message(message, check_for_none=False):
        """
        validates if a message is not null and it is of
        type string

        params:
            message (str): message to be vailidated
            check_for_none (bool): validate if message is none or emtpy
        """
        if message and not isinstance(message, str):
            raise TypeError("message must be a string")

        if check_for_none and not message:
            raise TypeError("message must not be empty!")


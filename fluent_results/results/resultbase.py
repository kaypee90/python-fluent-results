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

        if message and not isinstance(message, str):
            raise TypeError("message must be a string")

        if is_success and message:
            self.successes.append(message)

        if not is_success and message:
            self.errors.append(message)

    @property
    def is_failed(self):
        return not self.is_success


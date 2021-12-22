"""
Author kaypee90
"""

from abc import ABC
from results.custom_exceptions import MessageNotStringError, MessageNotEmptyError


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

        ResultBase._validate_message(message)

        if is_success and message:
            self.successes.append(message)

        if not is_success and message:
            self.errors.append(message)

    @property
    def is_failed(self):
        """
        Checks if the result is a failure
        """
        return not self.is_success

    def with_error(self, error_message):
        """
        takes in a error message and adds it to
        the list of error messages.

        params:
            error_message (str): message to be added
        returns
            ResultBase: an instance of result base
        """
        ResultBase._validate_message(error_message, True)
        self.errors.append(error_message)
        return self

    def with_errors(self, messages):
        """
        takes in a list of error messages and adds it to
        existing error message list.

        params:
            messages (list): message to be added to errors
        returns
            ResultBase: an instance of result base
        """
        self.errors.extend(messages)
        return self

    def with_success(self, success_message):
        """
        takes in a success message and adds it to
        the list of success messages.

        params:
            success_message (str): message to be added to successes
        returns
            ResultBase: an instance of result base
        """
        ResultBase._validate_message(success_message, True)
        self.successes.append(success_message)
        return self

    def with_successes(self, messages):
        """
        takes in a list of success messages and adds it to
        existing success message list.

        params:
            messages (list): message to be added to successes
        returns
            ResultBase: an instance of result base
        """
        self.successes.extend(messages)
        return self

    def with_reason(self, reason):
        """
        takes in a reason and adds it to
        the list of reasons.

        params:
            reason (str): message to be added to reasons
        returns
            ResultBase: an instance of result base
        """
        ResultBase._validate_message(reason, True)
        self.reasons.append(reason)
        return self

    def with_reasons(self, reasons):
        """
        takes in a list of reasons and adds it to
        existing reason list.

        params:
            reasons (list): message to be added to reasons
        returns
            ResultBase: an instance of result base
        """
        self.reasons.extend(reasons)
        return self

    def convert_to_dict(self):
        """
        Converts result object to a dict that can be searilized
        to JSON
        """
        return {
            "is_success": self.is_success,
            "value": self.value,
            "successes": self.successes,
            "errors": self.errors,
            "reasons": self.reasons,
        }

    @staticmethod
    def _validate_message(message, check_for_none=False):
        """
        validates if a message is not null and it is of
        type string

        params:
            message (str): message to be vailidated
            check_for_none (bool): validate if message is none or emtpy
        """
        if message and not isinstance(message, str):
            raise MessageNotStringError("message must be a string")

        if check_for_none and not message:
            raise MessageNotEmptyError("message must not be empty!")

    def __str__(self):
        """
        Get string representation of result object
        """
        if any(self.reasons):
            reasons = "; ".join(self.reasons)
            reasons_string = f", Reasons='{reasons}'"
            return f"Result: IsSuccess='{self.is_success}'{reasons_string}"

        return ""

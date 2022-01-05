"""
Author kaypee90
"""

from fluent_results.results.result_base import ResultBase


class Result(ResultBase):
    """
    Concrete class for holding results details
    """

    @classmethod
    def ok(cls, data=None, message=None):
        """
        Propates data and message for a successful process.
        
        params:
            data (any): data to be returned as part of Result object
            message (str): success message
        returns
            result: an instance of Result class
        """
        return cls(True, data, message)

    @classmethod
    def fail(cls, message=None):
        """
        Propates data and message for a failed process.
        
        params:
            message (str): error message
        returns
            result: an instance of Result class
        """
        return cls(False, None, message)

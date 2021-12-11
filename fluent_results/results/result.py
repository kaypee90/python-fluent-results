"""
Author kaypee90
"""

from .resultbase import ResultBase

class Result(ResultBase):
    """
    Concrete class for holding results details
    """
    def __init__(self, is_success, data, message):
        super(Result, self).__init__(is_success, data, message)

    @classmethod
    def ok(cls, data=None, message=None):
        """
        Handles successful data
        """
        return cls(True, data, message)

    @classmethod
    def fail(cls, message=None):
        """
        Handles failure information
        """
        return cls(False, None, message)

    


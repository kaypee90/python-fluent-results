"""
Author kaypee90
"""

from .resultbase import ResultBase

class Result(ResultBase):
    """
    Concrete class for holding results details
    """
    @classmethod
    def Ok(cls, message=None, **kwargs):
        """
        Handles successful data
        """
        if message:
            assert isinstance(message, str)
            cls.Successes.append(message)
        return cls


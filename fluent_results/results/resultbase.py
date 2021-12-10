"""
Author kaypee90
"""

from abc import ABC

class ResultBase(ABC):
    """
    Base class for all results
    """
    Errors = []

    Successes = []

    Reasons = []

    data = None

    @property
    def is_failed(self):
        return self.Errors.count() > 0

    @property
    def is_success(self):
        return not self.is_failed


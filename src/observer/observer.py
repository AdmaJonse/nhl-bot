"""
This module defines the observer of the subject.
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    This class defines the observer of the subject.
    """

    @abstractmethod
    def update(self, subject) -> None:
        """
        Receive an update from the subject.
        """

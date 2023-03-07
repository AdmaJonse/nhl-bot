"""
This module defines the subject being observed.
"""

from abc import ABC, abstractmethod

class Subject(ABC):
    """
    This class defines the subject being observed.
    """

    @abstractmethod
    def subscribe(self, observer) -> None:
        """
        The given observer subscribes to updates on this subject.
        """

    @abstractmethod
    def unsubscribe(self, observer) -> None:
        """
        The given observer unsubscribes to updates on this subject.
        """

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all subscribed observers about a change to the data.
        """

"""
Description:
    This module defines the Period Ready event.
"""

from src.events.event import Event
from src.utils import pad_code

class PeriodReady(Event):
    """
    Description:
        The Period Ready event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Period Ready - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PeriodReady) and
                isinstance(other, PeriodReady) and
                self.period == other.period)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PERREADY"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "PER" + str(self.period) + "-READY"

"""
This module defines the Period Official event.
"""

from src.events.event import Event
from src.utils import pad_code

class PeriodOfficial(Event):
    """
    The Period Official event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Period Official - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PeriodOfficial) and
                isinstance(other, PeriodOfficial) and
                self.period == other.period)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PEROFFICIAL"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "PER" + str(self.period.number) + "-OFFICIAL"

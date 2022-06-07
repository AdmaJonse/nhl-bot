"""
Description:
    This module defines the Period Ready event.
"""

from src.events.event import Event

class PeriodReady(Event):
    """
    Description:
        The Period Ready event.
    """

    def __str__(self):
        return str(self.time) + " = Period Ready - " + self.description

    def __eq__(self, other):
        return (isinstance(self, PeriodReady) and
                isinstance(other, PeriodReady) and
                self.period == other.period)

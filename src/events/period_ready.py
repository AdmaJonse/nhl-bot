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
        return str(self.event_id) + " = Period Ready - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period

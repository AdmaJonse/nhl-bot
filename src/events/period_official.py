"""
Description:
    This module defines the Period Official event.
"""
from src.events.event import Event

class PeriodOfficial(Event):
    """
    Description:
        The Period Official event.
    """

    def __str__(self):
        return str(self.event_id) + " = Period Official - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period

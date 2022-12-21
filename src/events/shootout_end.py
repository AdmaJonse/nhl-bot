"""
Description:
    This module defines the Shootout End event.
"""

from src.events.event import Event
from src.utils import pad_code

class ShootoutEnd(Event):
    """
    Description:
        The Shootout End event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Shootout End - " + self.description

    def __eq__(self, other):
        return (isinstance(self, ShootoutEnd) and
                isinstance(other, ShootoutEnd))

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "SOEND"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "SO-END"

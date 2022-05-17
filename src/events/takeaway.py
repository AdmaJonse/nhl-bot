"""
Description:
    This module defines the Takeaway event.
"""
from src.events.event import Event, get_player_name

class Takeaway(Event):
    """
    Description:
        The Takeaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.player = get_player_name(data, "PlayerID")

    def __str__(self):
        return str(self.event_id) + " = Takeaway - " + self.description

"""
Description:
    This module defines the Ping event.
"""

from typing import Optional

from src import templates
from src.events.event import Event, get_player_name
from src.game_data import GameData

class Ping(Event):
    """
    Description:
        The Ping event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.shooter   = get_player_name(data, "Shooter")
        self.goalie    = get_player_name(data, "Unknown")

        if "crossbar" in self.description.lower():
            self.goal_post = "crossbar"
        else:
            self.goal_post = "post"

    def __str__(self):
        return str(self.event_id) + " = Ping! - " + self.description

    @property
    def shooter(self) -> Optional[str]:
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def goalie(self) -> Optional[str]:
        """Getter for the goalie."""
        return self._goalie

    @goalie.setter
    def goalie(self, goalie : str):
        """Setter for the goalie."""
        self._goalie = goalie

    def get_post(self, game_data : GameData) -> Optional[str]:
        """
        Description:
            Return the event string for a ping event.
        """
        event_values = {
            "shooter":   self.shooter,
            "goalie":    self.goalie,
            "goal_post": self.goal_post,
            "hashtags":  game_data.hashtags
        }
        return templates.PING_TEMPLATE.format(**event_values)

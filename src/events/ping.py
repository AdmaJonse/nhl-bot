"""
This module defines the Ping event.
"""

from typing import Optional

from src.output import templates
from src.events.event import Event, get_player_name
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import initials, pad_blob, pad_code

class Ping(Event):
    """
    The Ping event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._shooter   : Optional[str] = get_player_name(data, "Shooter")
        self._goalie    : Optional[str] = get_player_name(data, "Unknown")
        self._goal_post : Optional[str] = None

        if "crossbar" in self.description.lower():
            self._goal_post = "crossbar"
        elif "post" in self.description.lower():
            self._goal_post = "post"

        if self.shooter is None:
            raise InsufficientData

        if self.goalie is None:
            raise InsufficientData

        if self.goal_post is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Ping! - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Ping) and
                isinstance(other, Ping) and
                self.period    == other.period and
                self.time      == other.time and
                self.shooter   == other.shooter and
                self.goalie    == other.goalie and
                self.goal_post == other.goal_post)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "PING"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        shooter : str = initials(self.shooter)
        goalie  : str = initials(self.goalie)
        blob    : str = shooter + "ON" + goalie
        return pad_blob(blob)

    @property
    def shooter(self) -> Optional[str]:
        """
        Getter for the shooter.
        """
        return self._shooter

    @shooter.setter
    def shooter(self, shooter : str):
        """
        Setter for the shooter.
        """
        self._shooter = shooter

    @property
    def goalie(self) -> Optional[str]:
        """
        Getter for the goalie.
        """
        return self._goalie

    @goalie.setter
    def goalie(self, goalie : str):
        """
        Setter for the goalie.
        """
        self._goalie = goalie

    @property
    def goal_post(self) -> Optional[str]:
        """
        Getter for the goal post.
        """
        return self._goal_post

    @goal_post.setter
    def goal_post(self, post : str):
        """
        Setter for the goal post.
        """
        self._goal_post = post

    def get_post(self, game_data : GameData, _line_score : LineScore) -> Optional[str]:
        """
        Return the event string for a ping event.
        """
        event_values = {
            "shooter":   self.shooter,
            "goalie":    self.goalie,
            "goal_post": self.goal_post,
            "hashtags":  game_data.hashtags
        }
        return templates.PING_TEMPLATE.format(**event_values)

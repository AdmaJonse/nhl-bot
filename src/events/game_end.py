"""
This module defines the Game End event.
"""

from typing import Optional

from src.data.line_score import LineScore
from src.output import templates
from src.events.event import Event
from src.data.game_data import GameData
from src.logger import log
from src.utils import pad_code

def winner(game_data: GameData, line_score: LineScore) -> str:
    """
    Return the winner of the game.
    """
    team: str = "Nobody"
    if line_score.is_home_winner:
        team = game_data.home.location
    elif line_score.is_away_winner:
        team = game_data.away.location
    else:
        log.error("Attempted to determine winner, but teams are tied.")
    return team

class GameEnd(Event):
    """
    The Game End event.
    """

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Game End - " + self.description

    def __eq__(self, other):
        return (isinstance(self, GameEnd) and
                isinstance(other, GameEnd))

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code: str = "GAMEEND"
        return pad_code(code)

    @property
    def id(self) -> str:
        return "GAME-END"

    def get_post(self, game_data: GameData, line_score: LineScore) -> Optional[str]:
        """
        Return the event string for a game end event.
        """
        output: str = ""
        event_values = {
            "winner":     winner(game_data, line_score),
            "home_team":  game_data.home.location,
            "away_team":  game_data.away.location,
            "home_goals": line_score.home_score,
            "away_goals": line_score.away_score,
            "hashtags":   game_data.hashtags
        }
        if self.period.is_overtime:
            output = templates.GAME_END_OT_TEMPLATE.format(**event_values)
        elif self.period.is_shootout:
            output = templates.GAME_END_SO_TEMPLATE.format(**event_values)
        else:
            output = templates.GAME_END_TEMPLATE.format(**event_values)
        return output

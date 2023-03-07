"""
This module handles parsing of the JSON line score data.
"""

from src.parser.parser import Parser
from src.stores import line_score
from src.data.line_score import LineScore

class LineScoreParser(Parser):
    """
    This class defines the parser for game data.
    """

    def __init__(self, game_id : int):
        super().__init__(game_id, "/feed/live")


    def parse(self):
        """
        Parse the static data for this game.
        """
        self.get_data()
        line_score.set_data(LineScore(self.data["liveData"]["linescore"]))

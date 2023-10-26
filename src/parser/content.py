"""
This module handles parsing of the JSON content data.
"""
from src.data.highlight import Highlight
from src.highlight_list import highlight_list
from src.parser.parser import Parser

GAME_CENTER_URL : str = "https://api-web.nhle.com/v1/gamecenter/"

class ContentParser(Parser):
    """
    This class defines the parser for the live feed data.
    """

    def __init__(self, game_id : int):
        super().__init__(game_id, "/landing", GAME_CENTER_URL)


    def parse(self):
        """
        Parse the content page for the current game to determine if there are any new
        highlights to post.
        """

        self.get_data()

        if self.data is None:
            return

        scoring_data = self.data.get("summary", {}).get("scoring", None)

        if scoring_data is None:
            return

        for period in scoring_data:
            for goal in period.get("goals", {}):

                if "highlightClip" not in goal:
                    continue

                highlight : Highlight = Highlight(goal)
                if not highlight_list.exists(highlight):
                    highlight_list.add(highlight)

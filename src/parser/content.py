"""
This module handles parsing of the JSON content data.
"""
from src.data.highlight import Highlight
from src.highlight_list import highlight_list
from src.parser.parser import Parser

class ContentParser(Parser):
    """
    This class defines the parser for the live feed data.
    """

    def __init__(self, game_id : int):
        super().__init__(game_id, "/content")


    def parse(self):
        """
        Parse the content page for the current game to determine if there are any new
        highlights to post.
        """

        self.get_data()
        if "hightlights" in self.data:
            for data in self.data["highlights"]["gameCenter"]["items"]:
                highlight : Highlight = Highlight(data)
                if not highlight_list.exists(highlight):
                    highlight_list.add(highlight)

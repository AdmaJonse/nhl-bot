"""
This module defines the Post Highlight command.
"""

from src.command.command import Command, Priority
from src.data.game_data import GameData
from src.data.highlight import Highlight
from src.output import output

class PostHighlight(Command):
    """
    This class defines the Post Highlight command.
    """

    def __init__(self, highlight : Highlight, parent : int, game_data : GameData):
        self.highlight  : Highlight = highlight
        self.parent     : int       = parent
        self.game_data  : GameData  = game_data
        super().__init__("Post Highlight", Priority.NORMAL)

    def execute(self) -> None:
        """
        Execute the command.
        """
        text = self.highlight.get_post(self.game_data)
        output.reply_with_media(self.parent, text, self.highlight.video)

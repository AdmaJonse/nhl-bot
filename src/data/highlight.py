"""
This module defines a highlight object.
"""

from src.data.game_data import GameData
from src.output import templates

VIDEO_FORMAT : str = "FLASH_1800K_896x504"

class Highlight:
    """
    This class defines a Highlight.
    """

    def __init__(self, data):
        self._id          : int = int(data["id"])
        self._event_id    : int = 0
        self._description : str = data["description"]
        self._video       : str = ""

        for keyword in data["keywords"]:
            if keyword["type"] == "statsEventId":
                self._event_id = int(keyword["value"])

        for video in data["playbacks"]:
            if video["name"] == VIDEO_FORMAT:
                self._video = video["url"]

    def __str__(self) -> str:
        """
        Return a string representing the highlight.
        """
        return "Highlight: "  + str(self._id)

    @property
    def id(self):
        """
        Return the ID for the highlight.
        """
        return self._id

    @property
    def event_id(self):
        """
        Return the event ID for the highlight.
        """
        return self._event_id

    @property
    def description(self):
        """
        Return the description the highlight.
        """
        return self._description

    @property
    def video(self):
        """
        Return the video URL for the highlight.
        """
        return self._video

    def get_post(self, game_data : GameData) -> str:
        """
        Create a post using the given highlight.
        """
        event_values = {
            "description": self.description,
            "hashtags":    game_data.hashtags
        }
        return templates.HIGHLIGHT_TEMPLATE.format(**event_values)

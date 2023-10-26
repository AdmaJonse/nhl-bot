"""
This module defines a highlight object.
"""

from src.data.abbreviations import to_location
from src.data.game_data import GameData
from src.output import templates

BASE_URL      : str = "https://players.brightcove.net/"
BRIGHTCOVE_ID : str = "6415718365001"
VIDEO_FORMAT  : str = "EXtG1xJ7H_default"
VIDEO_URL     : str = BASE_URL + BRIGHTCOVE_ID + "/" + VIDEO_FORMAT + "/index.html?videoId="

class Highlight:
    """
    This class defines a Highlight.
    """

    def __init__(self, data):
        self._id          : int = int(data["highlightClip"])
        self._goal_id     : int = int(data["homeScore"]) + int(data["awayScore"])
        self._video       : str = VIDEO_URL + str(self._id)
        self._description : str = ""

        # Construct the description
        player            : str = str(data["firstName"]) + " " + str(data["lastName"])
        abbreviation      : str = str(data["teamAbbrev"])
        team              : str = to_location.get(abbreviation, abbreviation)
        shot_type         : str = str(data["shotType"])
        self._description = player + " scores on a " + shot_type + " shot for " + team


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
    def goal_id(self):
        """
        Return the goal ID for the highlight.
        """
        return self._goal_id


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

"""
This module defines the Team class.
"""

from src.data.hashtags import hashtags, playoff_hashtags

class Team:
    """
    The team class. This class contains the various names that can be used for a team and
    provides methods for querying these names.
    """

    def __init__(self, data):
        self._location        : str = data["locationName"]
        self._team_name       : str = data["teamName"]
        self._abbreviation    : str = data["abbreviation"]
        self._full_name       : str = data["name"]
        self._timezone        : str = data["venue"]["timeZone"]["id"]
        self._hashtag         : str = hashtags[self._abbreviation]
        self._playoff_hashtag : str = playoff_hashtags[self._abbreviation]

    @property
    def location(self) -> str:
        """
        Getter for the team location.
        """
        return self._location

    @property
    def team_name(self) -> str:
        """
        Getter for the team name.
        """
        return self._team_name

    @property
    def abbreviation(self) -> str:
        """
        Getter for the team abbreviation.
        """
        return self._abbreviation

    @property
    def full_name(self) -> str:
        """
        Getter for the team full name.
        """
        return self._full_name

    @property
    def hashtag(self) -> str:
        """
        Getter for the team hashtag.
        """
        return self._hashtag

    @property
    def playoff_hashtag(self) -> str:
        """
        Getter for the team's playoff hashtag.
        """
        return self._playoff_hashtag

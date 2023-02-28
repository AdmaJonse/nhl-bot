"""
This module defines the Team class.
"""

class Team:
    """
    The team class. This class contains the various names that can be used for a team and
    provides methods for querying these names.
    """

    def __init__(self, data):
        self._location     : str = data["locationName"]
        self._team_name    : str = data["teamName"]
        self._abbreviation : str = data["abbreviation"]
        self._full_name    : str = data["name"]

    @property
    def location(self) -> str:
        """
        Getter for the team location.
        """
        return self._location

    @location.setter
    def location(self, location : str):
        """
        Setter for the team location.
        """
        self._location = location

    @property
    def team_name(self) -> str:
        """
        Getter for the team name.
        """
        return self._team_name

    @team_name.setter
    def team_name(self, name : str):
        """
        Setter for the team name.
        """
        self._team_name = name

    @property
    def abbreviation(self) -> str:
        """
        Getter for the team abbreviation.
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation : str):
        """
        Setter for the team abbreviation.
        """
        self._abbreviation = abbreviation

    @property
    def full_name(self) -> str:
        """
        Getter for the team full name.
        """
        return self._full_name

    @full_name.setter
    def full_name(self, name : str):
        """
        Setter for the team full name.
        """
        self._full_name = name

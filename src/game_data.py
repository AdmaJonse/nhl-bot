"""
Description:
    This module provides clases for storing and querying static game data. This data is
    initialized once for a particular game and will never change over the course of play.
"""

from typing import Any
from datetime import datetime
from dateutil import parser

from src import logger

TEAM_HASHTAG    = "#GoAvsGo"
PLAYOFF_HASHTAG = "#FindAWay"

class Team:
    """
    Description:
        The team class. This class contains the various names that can be used for a team and
        provides methods for querying these names.
    """

    def __init__(self, data):
        self._location     : str = data["locationName"]
        self._team_name    : str = data["teamName"]
        self._abbreviation : str = data["abbreviation"]
        self._full_name    : str = data["name"]

    @property
    def location(self):
        """Getter for the team location."""
        return self._location

    @location.setter
    def location(self, location):
        """Setter for the team location."""
        self._location = location

    @property
    def team_name(self):
        """Getter for the team name."""
        return self._team_name

    @team_name.setter
    def team_name(self, name):
        """Setter for the team name."""
        self._team_name = name

    @property
    def abbreviation(self):
        """Getter for the team abbreviation."""
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Setter for the team abbreviation."""
        self._abbreviation = abbreviation

    @property
    def full_name(self):
        """Getter for the team full name."""
        return self._full_name

    @full_name.setter
    def full_name(self, name):
        """Setter for the team full name."""
        self._full_name = name


class GameData:
    """
    Description:
        The GameData calss defines static data about the particular game, such as the teams
        that are playing and where the game is being played. This data will not change over the
        course of play.
    """

    def __init__(self, data):

        self._line_score  : Any       = data["liveData"]["linescore"]
        self._home        : Team      = Team(data["gameData"]["teams"]["home"])
        self._away        : Team      = Team(data["gameData"]["teams"]["away"])
        self._date        : datetime  = parser.parse(data["gameData"]["datetime"]["dateTime"])
        self._venue       : str       = data["gameData"]["teams"]["home"]["venue"]["name"]
        self._city        : str       = data["gameData"]["teams"]["home"]["venue"]["city"]
        self._is_playoffs : bool      = data["gameData"]["game"]["type"] == "P"

        self.print_constants()

    def print_constants(self):
        """
        Description:
            Log the class constants for the current game.
        """
        logger.log_info("Home Location:     " + self.home.location)
        logger.log_info("Home Team:         " + self.home.team_name)
        logger.log_info("Home Abbreviation: " + self.home.abbreviation)
        logger.log_info("Home Full Name:    " + self.home.full_name)
        logger.log_info("Away Location:     " + self.away.location)
        logger.log_info("Away Team:         " + self.away.team_name)
        logger.log_info("Away Abbreviation: " + self.away.abbreviation)
        logger.log_info("Away Full Name:    " + self.away.full_name)
        logger.log_info("Date/Time:         " + self.date.strftime("%I:%M %p %Z"))
        logger.log_info("Venue:             " + self.venue)
        logger.log_info("Is Playoffs:       " + str(self.is_playoffs))
        logger.log_info("Hashtags:          " + self.hashtags)


    def get_team_string(self, team : str) -> str:
        """
        Description:
            Return the name of the team from this event as a location name.
        """
        if team == self.home.full_name:
            team_string = self.home.location
        elif team == self.away.full_name:
            team_string = self.away.location
        else:
            logger.log_error("unknown team: " + team)
        return team_string


    def get_opposition(self, team : str) -> str:
        """
        Description:
            Return the opposing team's location name.
        """
        if team == self.home.full_name:
            team_string = self.away.location
        elif team == self.away.full_name:
            team_string = self.home.location
        else:
            logger.log_error("unknown team: " + team)
        return team_string


    @property
    def hashtags(self) -> str:
        """
        Description:
            Return the hashtags to append to all tweets.
        """
        hashtags = []
        hashtags.append("#" + self.away.abbreviation + "vs" + self.home.abbreviation)
        hashtags.append(TEAM_HASHTAG)
        if self.is_playoffs:
            hashtags.append(PLAYOFF_HASHTAG)
        return " ".join(hashtags)


    @property
    def home(self) -> Team:
        """Getter for the home team field."""
        return self._home


    @property
    def away(self) -> Team:
        """Getter for the away team field."""
        return self._away


    @property
    def date(self) -> datetime:
        """Getter for the date field."""
        return self._date


    @property
    def venue(self) -> str:
        """Getter for the venue field."""
        return self._venue


    @property
    def city(self) -> str:
        """Getter for the city field."""
        return self._city


    @property
    def is_playoffs(self) -> bool:
        """Getter for the is_playoffs field."""
        return self._is_playoffs


    @property
    def line_score(self) -> Any:
        """Getter for the line score."""
        return self._line_score


    @line_score.setter
    def line_score(self, data : Any):
        """
        Description:
            Update the line score record with the latest game data.
        """
        self._line_score = data


    @property
    def home_shots(self) -> int:
        """
        Description:
            Return the number of shots by the home team in the current line score.
        """
        return self.line_score["teams"]["home"]["shotsOnGoal"]


    @property
    def away_shots(self) -> int:
        """
        Description:
            Return the number of shots by the away team in the current line score.
        """
        return self.line_score["teams"]["away"]["shotsOnGoal"]

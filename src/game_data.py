"""
Description:
    This module provides clases for storing and querying static game data. This data is
    initialized once for a particular game and will never change over the course of play.
"""

from typing import Any, Optional
from datetime import datetime
from dateutil import parser

from src import line_score
from src import logger
from src.line_score import LineScore, PowerPlay
from src.team import Team

TEAM_HASHTAG    = "#GoAvsGo"
PLAYOFF_HASHTAG = "#FindAWay"

class GameData:
    """
    Description:
        The GameData calss defines static data about the particular game, such as the teams
        that are playing and where the game is being played. This data will not change over the
        course of play.
    """

    def __init__(self, data):

        self._line_score  : LineScore = LineScore(data["liveData"]["linescore"])
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


    def get_team_string(self, team : Optional[str]) -> str:
        """
        Description:
            Return the name of the team from this event as a location name.
        """
        if team == self.home.full_name:
            team_string = self.home.location
        elif team == self.away.full_name:
            team_string = self.away.location
        else:
            logger.log_error("unknown team: " + str(team))
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
        previous = self._line_score
        current  = LineScore(data)
        line_score.check_for_events(previous, current)
        self._line_score = current


    @property
    def home_shots(self) -> int:
        """
        Description:
            Return the number of shots by the home team in the current line score.
        """
        return self.line_score.home_shots


    @property
    def away_shots(self) -> int:
        """
        Description:
            Return the number of shots by the away team in the current line score.
        """
        return self.line_score.away_shots


    @property
    def power_play(self) -> Optional[PowerPlay]:
        """
        Description:
            Getter for the power play record.
        """
        return self.line_score.power_play

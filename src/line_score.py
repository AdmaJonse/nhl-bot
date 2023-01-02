"""
Description:
    This module contains classes used to define line score data.
"""

from dataclasses import dataclass
import time
from typing import Optional

from src import logger

@dataclass
class TeamData:
    """
    Description:
        This data class defines data that is specific to one team.
    """
    shots          : int  = 0
    goals          : int  = 0
    goalie_pulled  : bool = False
    skater_count   : int  = 0
    is_power_play  : bool = False


@dataclass
class PowerPlay:
    """
    Description:
        This data class defines a power play.
    """
    team           : Optional[str]  = ""
    home_skaters   : int  = 0
    away_skaters   : int  = 0
    strength       : str  = ""
    time_remaining : str  = "00:00"
    time_elapsed   : str  = "00:00"


def get_power_play(data) -> Optional[PowerPlay]:
    """
    Description:
        Create a power play object using line score data.
    """

    strength        : str  = data["powerPlayStrength"]
    home_skaters    : int  = data["teams"]["home"]["numSkaters"]
    home_power_play : bool = data["teams"]["home"]["powerPlay"]
    away_skaters    : int  = data["teams"]["away"]["numSkaters"]
    away_power_play : bool = data["teams"]["away"]["powerPlay"]

    try:

        time_remaining  : int  = data["powerPlayInfo"]["situationtime_remainingaining"]
        time_elapsed    : int  = data["powerPlayInfo"]["situationTimeElapsed"]
        in_situation    : bool = data["powerPlayInfo"]["inSituation"]

    except KeyError:

        time_remaining = 0
        time_elapsed   = 0
        in_situation   = False


    if not in_situation:
        return None

    if home_power_play:

        if home_skaters <= away_skaters:
            logger.log_error("Line score indicates home powerplay, but skater counts are wrong.")
            logger.log_error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "home"

    elif away_power_play:

        if home_skaters >= away_skaters:
            logger.log_error("Line score indicates away powerplay, but skater counts are wrong.")
            logger.log_error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "away"

    else:

        if home_skaters != away_skaters:
            logger.log_error("Line score indicates even strength, but skater counts are wrong.")
            logger.log_error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "even"

    return PowerPlay (
        team           = team,
        home_skaters   = home_skaters,
        away_skaters   = away_skaters,
        strength       = strength,
        time_remaining = time.strftime("%M:%S", time.gmtime(time_remaining)),
        time_elapsed   = time.strftime("%M:%S", time.gmtime(time_elapsed))
    )


@dataclass
class ShootoutData:
    """
    Description:
        This data class defines data for a shootout event.
    """
    home_goals    : int = 0
    home_attempts : int = 0
    away_goals    : int = 0
    away_attempts : int = 0


def get_shootout(data) -> Optional[ShootoutData]:
    """
    Description:
        Create a shootout data object using line score data.
    """

    home_goals    : int = 0
    home_attempts : int = 0
    away_goals    : int = 0
    away_attempts : int = 0

    if data["hasShootout"]:

        home_goals    = data["shootoutInfo"]["home"]["scores"]
        home_attempts = data["shootoutInfo"]["home"]["attempts"]
        away_goals    = data["shootoutInfo"]["away"]["scores"]
        away_attempts = data["shootoutInfo"]["away"]["attempts"]

        return ShootoutData (
            home_goals    = home_goals,
            home_attempts = home_attempts,
            away_goals    = away_goals,
            away_attempts = away_attempts
        )

    return None


class LineScore:
    """
    Description:
        This class defines line score data.
    """

    def __init__(self, data):
        self.home : TeamData = TeamData(
            shots         = data["teams"]["home"]["shotsOnGoal"],
            goals         = data["teams"]["home"]["goals"],
            goalie_pulled = data["teams"]["home"]["goaliePulled"],
            skater_count  = data["teams"]["home"]["numSkaters"],
            is_power_play = data["teams"]["home"]["powerPlay"]
        )
        self.away : TeamData = TeamData(
            shots         = data["teams"]["away"]["shotsOnGoal"],
            goals         = data["teams"]["away"]["goals"],
            goalie_pulled = data["teams"]["away"]["goaliePulled"],
            skater_count  = data["teams"]["away"]["numSkaters"],
            is_power_play = data["teams"]["away"]["powerPlay"]
        )
        self.power_play : Optional[PowerPlay]    = get_power_play(data)
        self.shootout   : Optional[ShootoutData] = get_shootout(data)


    def __eq__(self, other):
        return (self.home == other.home and
                self.away == other.away and
                self.power_play == other.power_play and
                self.shootout == other.shootout)

    def __str__(self):
        chunks = []
        chunks.append("Line Score: ")
        chunks.append("Home: ")
        chunks.append("  Shots:             " + str(self.home.shots))
        chunks.append("  Goals:             " + str(self.home.goals))
        chunks.append("  Goalie Pulled:     " + str(self.home.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self.home.skater_count))
        chunks.append("  Is Power Play:     " + str(self.home.is_power_play))
        chunks.append("Away: ")
        chunks.append("  Shots:             " + str(self.away.shots))
        chunks.append("  Goals:             " + str(self.away.goals))
        chunks.append("  Goalie Pulled:     " + str(self.away.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self.away.skater_count))
        chunks.append("  Is Power Play:     " + str(self.away.is_power_play))

        if self.power_play is not None:
            chunks.append("Power Play: ")
            chunks.append("  Team:              " + str(self.power_play.team))
            chunks.append("  Strength:          " + str(self.power_play.strength))
            chunks.append("  Time Remaining:    " + str(self.power_play.time_remaining))
            chunks.append("  Time Elapsed:      " + str(self.power_play.time_elapsed))

        if self.shootout is not None:
            chunks.append("Shootout: ")
            chunks.append("  Home Goals:        " + str(self.shootout.home_goals))
            chunks.append("  Home Attempts:     " + str(self.shootout.home_attempts))
            chunks.append("  Away Goals:        " + str(self.shootout.away_goals))
            chunks.append("  Away Attempts:     " + str(self.shootout.away_attempts))

        return '\n'.join(chunks)


    @property
    def home_shots(self) -> int:
        """
        Description:
            Getter for the home shots value.
        """
        return self.home.shots


    @property
    def away_shots(self) -> int:
        """
        Description:
            Getter for the away shots value.
        """
        return self.away.shots


    @property
    def home_goals(self) -> int:
        """
        Description:
            Getter for the home goals value.
        """
        return self.home.goals


    @property
    def away_goals(self) -> int:
        """
        Description:
            Getter for the away goals value.
        """
        return self.away.goals


    @property
    def home_goalie_pulled(self) -> bool:
        """
        Description:
            Getter for the home goalie pulled value.
        """
        return self.home.goalie_pulled


    @property
    def away_goalie_pulled(self) -> bool:
        """
        Description:
            Getter for the away goalie pulled value.
        """
        return self.away.goalie_pulled


    @property
    def home_shootout_goals(self) -> int:
        """
        Description:
            Getter for the home shootout goals value.
        """
        if self.shootout is None:
            return 0
        return self.shootout.home_goals


    @property
    def away_shootout_goals(self) -> int:
        """
        Description:
            Getter for the away shotoout goals value.
        """
        if self.shootout is None:
            return 0
        return self.shootout.away_goals


def check_for_events(previous : 'LineScore', current : 'LineScore'):
    """
    Description:
        Check if an event has occured in the line score data that requires a post.
    """

    if previous.home_goalie_pulled != current.home_goalie_pulled:
        if current.home_goalie_pulled:
            logger.log_info("The home team has pulled their goalie.")
        else:
            logger.log_info("The home goalie has returned to the net.")

    if previous.away_goalie_pulled != current.away_goalie_pulled:
        if current.away_goalie_pulled:
            logger.log_info("The away team has pulled their goalie.")
        else:
            logger.log_info("The away goalie has returned to the net.")

    if previous.power_play != current.power_play:
        if current.power_play is None:
            logger.log_info("The teams are even strength")
        elif current.home.skater_count > current.away.skater_count:
            logger.log_info("The home team is on a power play: " + str(current.power_play.strength))
        elif current.home.skater_count < current.away.skater_count:
            logger.log_info("The away team is on a power play: " + str(current.power_play.strength))

"""
Description:
    TODO
"""

from dataclasses import dataclass
import time
from typing import Optional

from src import logger

@dataclass
class TeamData:
    """
    Description:
        TODO
    """
    shots          : int  = 0
    goalie_pulled  : bool = False
    skater_count   : int  = 0
    is_power_play  : bool = False


@dataclass
class PowerPlay:
    """
    Description:
        TODO
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
    time_remaining  : int  = data["powerPlayInfo"]["situationTimeRemaining"]
    time_elapsed    : int  = data["powerPlayInfo"]["situationTimeElapsed"]
    in_situation    : bool = data["powerPlayInfo"]["inSituation"]
    home_skaters    : int  = data["teams"]["home"]["numSkaters"]
    home_power_play : bool = data["teams"]["home"]["powerPlay"]
    away_skaters    : int  = data["teams"]["away"]["numSkaters"]
    away_power_play : bool = data["teams"]["away"]["powerPlay"]

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

    power_play : PowerPlay = PowerPlay(
        team           = team,
        home_skaters   = home_skaters,
        away_skaters   = away_skaters,
        strength       = strength,
        time_remaining = time.strftime("%M:%S", time.gmtime(time_remaining)),
        time_elapsed   = time.strftime("%M:%S", time.gmtime(time_elapsed))
    )

    return power_play


class LineScore:
    """
    Description:
        TODO
    """

    def __init__(self, data):
        self.home : TeamData = TeamData(
            shots         = data["teams"]["home"]["shotsOnGoal"],
            goalie_pulled = data["teams"]["home"]["goaliePulled"],
            skater_count  = data["teams"]["home"]["numSkaters"],
            is_power_play = data["teams"]["home"]["powerPlay"]
        )
        self.away : TeamData = TeamData(
            shots         = data["teams"]["away"]["shotsOnGoal"],
            goalie_pulled = data["teams"]["away"]["goaliePulled"],
            skater_count  = data["teams"]["away"]["numSkaters"],
            is_power_play = data["teams"]["away"]["powerPlay"]
        )
        self.power_play : Optional[PowerPlay] = get_power_play(data)


    def __eq__(self, other):
        return (self.home != other.home or
                self.away != other.away or
                self.power_play != other.power_play)

    def __str__(self):
        chunks = []
        chunks.append("Line Score: ")
        chunks.append("Home: ")
        chunks.append("  Shots:             " + str(self.home.shots))
        chunks.append("  Goalie Pulled:     " + str(self.home.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self.home.skater_count))
        chunks.append("  Is Power Play:     " + str(self.home.is_power_play))
        chunks.append("Away: ")
        chunks.append("  Shots:             " + str(self.away.shots))
        chunks.append("  Goalie Pulled:     " + str(self.away.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self.away.skater_count))
        chunks.append("  Is Power Play:     " + str(self.away.is_power_play))
        chunks.append("Power Play: ")
        chunks.append("  Team:              " + str(self.power_play.team))
        chunks.append("  Strength:          " + str(self.power_play.strength))
        chunks.append("  Time Remaining:    " + str(self.power_play.time_remaining))
        chunks.append("  Time Elapsed:      " + str(self.power_play.time_elapsed))
        return '\n'.join(chunks)


    @property
    def home_shots(self) -> int:
        """
        Description:
            Getter for the home shots value.
        """
        return self.home.shots


    @home_shots.setter
    def home_shots(self, shots : int):
        """
        Description:
            Setter for the home shots value.
        """
        self.home.shots = shots


    @property
    def away_shots(self) -> int:
        """
        Description:
            Getter for the away shots value.
        """
        return self.away.shots


    @away_shots.setter
    def away_shots(self, shots : int):
        """
        Description:
            Setter for the away shots value.
        """
        self.away.shots = shots


    @property
    def home_goalie_pulled(self) -> bool:
        """
        Description:
            Getter for the home goalie pulled value.
        """
        return self.home.goalie_pulled


    @home_goalie_pulled.setter
    def home_goalie_pulled(self, is_pulled : bool):
        """
        Description:
            Setter for the home goalie pulled value.
        """
        self.home.goalie_pulled = is_pulled


    @property
    def away_goalie_pulled(self) -> bool:
        """
        Description:
            Getter for the away goalie pulled value.
        """
        return self.away.goalie_pulled


    @away_goalie_pulled.setter
    def away_goalie_pulled(self, is_pulled : bool):
        """
        Description:
            Setter for the away goalie pulled value.
        """
        self.away.goalie_pulled = is_pulled


    @property
    def power_play(self) -> Optional[PowerPlay]:
        """
        Description:
            Getter for the power play record.
        """
        return self._power_play


    @power_play.setter
    def power_play(self, power_play : Optional[PowerPlay]):
        """
        Description:
            Setter for the power play record.
        """
        self._power_play = power_play


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
            logger.log_info("The home team has pulled their goalie.")
        else:
            logger.log_info("The home goalie has returned to the net.")

    if previous.power_play != current.power_play:
        if current.power_play is None:
            logger.log_info("The teams are even strength")
        elif current.home.skater_count > current.away.skater_count:
            logger.log_info("The home team is on a power play: " + str(current.power_play.strength))
        elif current.home.skater_count < current.away.skater_count:
            logger.log_info("The away team is on a power play: " + str(current.power_play.strength))

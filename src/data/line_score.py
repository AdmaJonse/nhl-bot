"""
This module contains classes used to define line score data.
"""

from typing import Optional
from src import logger

from src.data.power_play import PowerPlay, get_power_play
from src.data.shootout import ShootoutData, get_shootout
from src.data.team_data import TeamData

class LineScore:
    """
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
        Getter for the home shots value.
        """
        return self.home.shots


    @property
    def away_shots(self) -> int:
        """
        Getter for the away shots value.
        """
        return self.away.shots


    @property
    def home_goals(self) -> int:
        """
        Getter for the home goals value.
        """
        return self.home.goals


    @property
    def away_goals(self) -> int:
        """
        Getter for the away goals value.
        """
        return self.away.goals


    @property
    def home_goalie_pulled(self) -> bool:
        """
        Getter for the home goalie pulled value.
        """
        return self.home.goalie_pulled


    @property
    def away_goalie_pulled(self) -> bool:
        """
        Getter for the away goalie pulled value.
        """
        return self.away.goalie_pulled


    @property
    def home_shootout_goals(self) -> int:
        """
        Getter for the home shootout goals value.
        """
        if self.shootout is None:
            return 0
        return self.shootout.home_goals


    @property
    def away_shootout_goals(self) -> int:
        """
        Getter for the away shotoout goals value.
        """
        if self.shootout is None:
            return 0
        return self.shootout.away_goals


def check_for_events(previous : 'LineScore', current : 'LineScore'):
    """
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

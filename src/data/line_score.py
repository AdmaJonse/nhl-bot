"""
This module contains classes used to define line score data.
"""

from typing import Optional
from src.logger import log

from src.data.power_play import PowerPlay, get_power_play
from src.data.shootout import ShootoutData, get_shootout
from src.data.team_data import TeamData

class LineScore:
    """
    This class defines line score data.
    """

    def __init__(self, data):
        self._home : TeamData = TeamData(
            shots         = data["teams"]["home"]["shotsOnGoal"],
            goals         = data["teams"]["home"]["goals"],
            goalie_pulled = data["teams"]["home"]["goaliePulled"],
            skater_count  = data["teams"]["home"]["numSkaters"],
            is_power_play = data["teams"]["home"]["powerPlay"]
        )
        self._away : TeamData = TeamData(
            shots         = data["teams"]["away"]["shotsOnGoal"],
            goals         = data["teams"]["away"]["goals"],
            goalie_pulled = data["teams"]["away"]["goaliePulled"],
            skater_count  = data["teams"]["away"]["numSkaters"],
            is_power_play = data["teams"]["away"]["powerPlay"]
        )
        self._power_play : Optional[PowerPlay]    = get_power_play(data)
        self._shootout   : Optional[ShootoutData] = get_shootout(data)


    def __eq__(self, other):
        return (self is not None and
                other is not None and
                self._home == other._home and
                self._away == other._away and
                self._power_play == other._power_play and
                self._shootout == other._shootout)

    def __str__(self):
        chunks = []
        chunks.append("Line Score: ")
        chunks.append("Home: ")
        chunks.append("  Shots:             " + str(self._home.shots))
        chunks.append("  Goals:             " + str(self._home.goals))
        chunks.append("  Goalie Pulled:     " + str(self._home.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self._home.skater_count))
        chunks.append("  Is Power Play:     " + str(self._home.is_power_play))
        chunks.append("Away: ")
        chunks.append("  Shots:             " + str(self._away.shots))
        chunks.append("  Goals:             " + str(self._away.goals))
        chunks.append("  Goalie Pulled:     " + str(self._away.goalie_pulled))
        chunks.append("  Number of Skaters: " + str(self._away.skater_count))
        chunks.append("  Is Power Play:     " + str(self._away.is_power_play))

        if self._power_play is not None:
            chunks.append("Power Play: ")
            chunks.append("  Team:              " + str(self._power_play.team))
            chunks.append("  Strength:          " + str(self._power_play.strength))
            chunks.append("  Time Remaining:    " + str(self._power_play.time_remaining))
            chunks.append("  Time Elapsed:      " + str(self._power_play.time_elapsed))

        if self._shootout is not None:
            chunks.append("Shootout: ")
            chunks.append("  Home Goals:        " + str(self._shootout.home_goals))
            chunks.append("  Home Attempts:     " + str(self._shootout.home_attempts))
            chunks.append("  Away Goals:        " + str(self._shootout.away_goals))
            chunks.append("  Away Attempts:     " + str(self._shootout.away_attempts))

        return '\n'.join(chunks)


    @property
    def home_shots(self) -> int:
        """
        Getter for the home shots value.
        """
        return self._home.shots


    @property
    def away_shots(self) -> int:
        """
        Getter for the away shots value.
        """
        return self._away.shots


    @property
    def home_goals(self) -> int:
        """
        Getter for the home goals value.
        """
        return self._home.goals


    @property
    def away_goals(self) -> int:
        """
        Getter for the away goals value.
        """
        return self._away.goals


    @property
    def home_goalie_pulled(self) -> bool:
        """
        Getter for the home goalie pulled value.
        """
        return self._home.goalie_pulled


    @property
    def away_goalie_pulled(self) -> bool:
        """
        Getter for the away goalie pulled value.
        """
        return self._away.goalie_pulled


    @property
    def home_shootout_goals(self) -> int:
        """
        Getter for the home shootout goals value.
        """
        if self._shootout is None:
            return 0
        return self._shootout.home_goals


    @property
    def away_shootout_goals(self) -> int:
        """
        Getter for the away shootout goals value.
        """
        if self._shootout is None:
            return 0
        return self._shootout.away_goals


    @property
    def is_home_winner(self) -> bool:
        """
        Return a boolean indicating whether or not the home team has won the game.
        """
        is_winner : bool = self.home_goals > self.away_goals

        if self._shootout is not None:
            is_winner = self.home_shootout_goals > self.away_shootout_goals

        return is_winner


    @property
    def is_away_winner(self) -> bool:
        """
        Return a boolean indicating whether or not the away team has won the game.
        """
        is_winner : bool = self.away_goals > self.home_goals

        if self._shootout is not None:
            is_winner = self.away_shootout_goals > self.home_shootout_goals

        return is_winner

    @property
    def home_score(self) -> int:
        """
        Slightly different from goals because we'll add the extra goal in
        the event of a shootout win.
        """
        score : int = self.home_goals
        if self._shootout is not None and self.is_home_winner:
            score += 1
        return score


    @property
    def away_score(self) -> int:
        """
        Slightly different from goals because we'll add the extra goal in
        the event of a shootout win.
        """
        score : int = self.away_goals
        if self._shootout is not None and self.is_away_winner:
            score += 1
        return score


    @property
    def power_play(self) -> Optional[PowerPlay]:
        """
        Accessor for the power play property.
        """
        return self._power_play


    @property
    def home(self) -> TeamData:
        """
        Accessor for the home team property.
        """
        return self._home


    @property
    def away(self) -> TeamData:
        """
        Accessor for the home team property.
        """
        return self._home


def check_for_events(previous : 'LineScore', current : 'LineScore'):
    """
    Check if an event has occurred in the line score data that requires a post.
    """

    if previous.home_goalie_pulled != current.home_goalie_pulled:
        if current.home_goalie_pulled:
            log.info("The home team has pulled their goalie.")
        else:
            log.info("The home goalie has returned to the net.")

    if previous.away_goalie_pulled != current.away_goalie_pulled:
        if current.away_goalie_pulled:
            log.info("The away team has pulled their goalie.")
        else:
            log.info("The away goalie has returned to the net.")

    if previous.power_play != current.power_play:
        if current.power_play is None:
            log.info("The teams are even strength")
        elif current.home.skater_count > current.away.skater_count:
            log.info("The home team is on a power play: " + str(current.power_play.strength))
        elif current.home.skater_count < current.away.skater_count:
            log.info("The away team is on a power play: " + str(current.power_play.strength))

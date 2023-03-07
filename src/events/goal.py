"""
This module defines the Goal event.
"""

from typing import Optional

from src.logger import log
from src.output import templates
from src.events.event import Event, get_player_name, get_team, get_value
from src.exceptions import InsufficientData
from src.data.game_data import GameData
from src.data.line_score import LineScore
from src.utils import initials, pad_blob, pad_code

class Goal(Event):
    """
    The Goal event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._team             : Optional[str] = get_team(data)
        self._scorer           : Optional[str] = get_player_name(data, "Scorer")
        self._primary_assist   : Optional[str] = get_player_name(data, "Assist", 1)
        self._secondary_assist : Optional[str] = get_player_name(data, "Assist", 2)
        self._goalie           : Optional[str] = get_player_name(data, "Goalie")
        self._strength         : Optional[str] = get_value(data, "result", "strength", "code")
        self._is_empty_net     : bool          = get_value(data, "result", "emptyNet")

        if self.team is None:
            raise InsufficientData

        if self.scorer is None:
            raise InsufficientData

        if self.goalie is None:
            raise InsufficientData

    def __str__(self):
        return str(self.id) + " - " + str(self.time) + " = Goal - " + self.description

    def __eq__(self, other):
        return (isinstance(self, Goal) and
                isinstance(other, Goal) and
                self.period           == other.period and
                self.time             == other.time and
                self.scorer           == other.scorer and
                self.primary_assist   == other.primary_assist and
                self.secondary_assist == other.secondary_assist and
                self.goalie           == other.goalie and
                self.strength         == other.strength and
                self.is_empty_net     == other.is_empty_net and
                self.team             == other.team)

    @property
    def code(self) -> str:
        """
        Return a seven-character code representing the event type.
        """
        code : str = "GOAL"
        return pad_code(code)

    @property
    def blob(self) -> str:
        """
        Return a unique identifier that describes this specific event.
        """
        # We need to account for possible changes to scorer, assists, etc, so we
        # avoid using player names in the blob. We'll just use the score here
        # since it should theoretically always be the same for a specific goal.

        home : str = str(self.score.home_goals)
        away : str = str(self.score.away_goals)
        blob : str = home + "TO" + away

        # Shootout goals are special because the score doesn't change. Need to
        # account for this by IDing them separately.

        if self.period.is_shootout:
            shooter : str = initials(self.scorer)
            goalie  : str = initials(self.goalie)
            blob = shooter + "ON" + goalie

        return pad_blob(blob)

    @property
    def team(self) -> Optional[str]:
        """
        Getter for the team.
        """
        return self._team

    @team.setter
    def team(self, team : str):
        """
        Setter for the team.
        """
        self._team = team

    @property
    def scorer(self) -> Optional[str]:
        """
        Getter for the scorer.
        """
        return self._scorer

    @scorer.setter
    def scorer(self, scorer : str):
        """
        Setter for the scorer.
        """
        self._scorer = scorer

    @property
    def primary_assist(self) -> Optional[str]:
        """
        Getter for the primary assist.
        """
        return self._primary_assist

    @primary_assist.setter
    def primary_assist(self, primary_assist : str):
        """
        Setter for the primary assist.
        """
        self._primary_assist = primary_assist

    @property
    def secondary_assist(self) -> Optional[str]:
        """
        Getter for the secondary assist.
        """
        return self._secondary_assist

    @secondary_assist.setter
    def secondary_assist(self, secondary_assist : str):
        """
        Setter for the secondary assist.
        """
        self._secondary_assist = secondary_assist

    @property
    def goalie(self) -> Optional[str]:
        """
        Getter for the goalie.
        """
        return self._goalie

    @goalie.setter
    def goalie(self, goalie : str):
        """
        Setter for the goalie.
        """
        self._goalie = goalie

    @property
    def strength(self) -> Optional[str]:
        """
        Getter for the strength.
        """
        return self._strength

    @strength.setter
    def strength(self, strength : str):
        """
        Setter for the strength.
        """
        self._strength = strength

    @property
    def is_empty_net(self) -> bool:
        """
        Getter for the is_empty_net property.
        """
        return self._is_empty_net

    @is_empty_net.setter
    def is_empty_net(self, is_empty_net : bool):
        """
        Setter for the is_empty_net property.
        """
        self._is_empty_net = is_empty_net

    def get_post(self : 'Goal', game_data : GameData, _line_score : LineScore) -> Optional[str]:
        """
        Return the event string for a goal event.
        """

        if self.scorer is None:
            log.error("Could not determine goal scorer. Delaying tweet.")
            return None

        goal_string   : str = ""
        assist_string : str = ""
        footer        : str = ""

        event_values = {
            "team":             game_data.get_team_string(self.team),
            "scorer":           self.scorer,
            "goalie":           self.goalie,
            "primary_assist":   self.primary_assist,
            "secondary_assist": self.secondary_assist,
            "description":      self.description,
            "time":             self.time,
            "period":           self.period.ordinal,
            "home_team":        game_data.home.location,
            "away_team":        game_data.away.location,
            "home_goals":       self.score.home_goals,
            "away_goals":       self.score.away_goals,
            "hashtags":         game_data.hashtags
        }

        if self.period.is_shootout:
            return templates.SHOOTOUT_GOAL_TEMPLATE.format(**event_values)

        if self.is_empty_net:
            goal_string = templates.EMPTY_NET_GOAL_TEMPLATE.format(**event_values)
        elif self.strength == "PPG":
            goal_string = templates.POWER_PLAY_GOAL_TEMPLATE.format(**event_values)
        elif self.strength == "SHG":
            goal_string = templates.SHORT_HANDED_GOAL_TEMPLATE.format(**event_values)
        else:
            goal_string = templates.GOAL_TEMPLATE.format(**event_values)

        if self.secondary_assist is not None:
            assist_string = templates.TWO_ASSIST_TEMPLATE.format(**event_values)
        elif self.primary_assist is not None:
            assist_string = templates.ONE_ASSIST_TEMPLATE.format(**event_values)

        footer = templates.GOAL_FOOTER_TEMPLATE.format(**event_values)

        return goal_string + assist_string + footer


    def is_scorer_modified(self, other : 'Goal') -> bool:
        """
        Return a boolean indicating whether the scorer is different in the given goal events.
        """
        return self.scorer is not None and other.scorer != self.scorer


    def is_primary_assist_added(self, other : 'Goal') -> bool:
        """
        Return a boolean indicating whether a primary assist has been added between goal events.
        """
        return other.primary_assist is None and self.primary_assist is not None


    def get_reply(self, game : GameData, _line : LineScore, previous : Event) -> Optional[str]:
        """
        Return the reply string for a goal event.
        """

        if not isinstance(previous, Goal):
            log.error("Attempted to call Goal reply with type: " + str(previous.__class__))
            return None

        # Sometimes the NHL will remove all the data from a goal event after it's been posted.
        # When that happens, we want to avoid posting a reply so that we don't spam tweets.
        if self.scorer is None:
            return None

        event_values = {
            "team":             game.get_team_string(self.team),
            "scorer":           self.scorer,
            "primary_assist":   self.primary_assist,
            "secondary_assist": self.secondary_assist,
            "description":      self.description,
            "time":             self.time,
            "period":           self.period.ordinal,
            "home_team":        game.home.location,
            "away_team":        game.away.location,
            "home_goals":       self.score.home_goals,
            "away_goals":       self.score.away_goals,
            "hashtags":         game.hashtags
        }

        scorer_modified      : bool = self.is_scorer_modified(previous)
        primary_assist_added : bool = self.is_primary_assist_added(previous)

        secondary_assist_added : bool = (
            previous.secondary_assist is None and
            self.secondary_assist is not None
        )

        primary_assist_modified : bool = (
            previous.primary_assist is not None and
            self.primary_assist is not None and
            previous.primary_assist != self.primary_assist
        )

        secondary_assist_modified : bool = (
            previous.secondary_assist is not None and
            self.secondary_assist is not None and
            previous.secondary_assist != self.secondary_assist
        )

        update_text : Optional[str] = None

        # Time of goal has been changed
        if previous.time != self.time:
            update_text = templates.GOAL_TIME_UPDATE_TEMPLATE.format(**event_values)

        # Assists have been changed
        if primary_assist_modified and secondary_assist_modified:
            update_text = templates.ASSIST_UPDATE_TEMPLATE.format(**event_values)
        elif primary_assist_modified:
            update_text = templates.PRIMARY_ASSIST_UPDATE_TEMPLATE.format(**event_values)
        elif secondary_assist_modified:
            update_text = templates.SECONDARY_ASSIST_UPDATE_TEMPLATE.format(**event_values)

        # Assists have been added
        if primary_assist_added and secondary_assist_added:
            update_text = templates.ASSIST_ADD_BOTH_TEMPLATE.format(**event_values)
        elif primary_assist_added:
            update_text = templates.ASSIST_ADD_PRIMARY_TEMPLATE.format(**event_values)
        elif secondary_assist_added:
            update_text = templates.ASSIST_ADD_SECONDARY_TEMPLATE.format(**event_values)

        # Goal scorer has been changed
        if scorer_modified:
            update_text = templates.SCORER_UPDATE_TEMPLATE.format(**event_values)

        return update_text

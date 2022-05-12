"""
Description:
    This module defines event classes. Event data is parsed from the
    NHL API JSON data and converted into Event objects.

    The main benefit of an object-based approach rather than simply
    comparing the JSON data itself, is that it makes comparisons
    between events far simpler. We have more control over the
    comparisons themselves and we're no longer going to trigger event
    update processing when minor JSON fields change as opposed to
    relevant event data.
"""
from enum import Enum
from src import logger

# pylint: disable=too-few-public-methods

class Events(Enum):
    """
    Description:
        The event type enumeration.
    """
    BLOCKED_SHOT_EVENT    = "Blocked Shot"
    CHALLENGE_EVENT       = "Official Challenge"
    FACEOFF_EVENT         = "Faceoff"
    GAME_END_EVENT        = "Game End"
    GAME_OFFICIAL_EVENT   = "Game Official"
    GAME_SCHEDULED_EVENT  = "Game Scheduled"
    GIVEAWAY_EVENT        = "Giveaway"
    GOAL_EVENT            = "Goal"
    HIT_EVENT             = "Hit"
    MISSED_SHOT_EVENT     = "Missed Shot"
    PENALTY_EVENT         = "Penalty"
    PENALTY_SHOT_EVENT    = "Penalty Shot"
    PERIOD_END_EVENT      = "Period End"
    PERIOD_OFFICIAL_EVENT = "Period Official"
    PERIOD_READY_EVENT    = "Period Ready"
    PERIOD_START_EVENT    = "Period Start"
    SHOT_EVENT            = "Shot"
    STOPPAGE_EVENT        = "Stoppage"
    TAKEAWAY_EVENT        = "Takeaway"


def get_player_name(event, player_type, index=1):
    """
    Description:
        Return the name of the player with the given type from the event.
    """
    count = 0
    try:
        for player in event["players"]:
            if player["playerType"].lower() == player_type.lower():
                count += 1
                if count == index:
                    return player["player"]["fullName"]
    except KeyError:
        return None

    return None


def get_team(event):
    """
    Description:
        Return the name of the team in the given event. Log an error
        and return None if no team was found.
    """
    try:
        return event["team"]["name"]
    except KeyError:
        logger.log_info("Could not find team.")
        return None


def get_value(data, *args):
    """
    Description:
        Helper function for retrieving values from multi-level dictionaries.
        If the key is not found, return an empty string.
    """
    for key in args:
        try:
            value = data.get(key)
            data = value
        except KeyError:
            logger.log_error("Could not find key: " + key)
            return None
        except AttributeError:
            logger.log_error("Could not find key: " + key)
            return None
    return value


class Event:
    """
    Description:
        The base event class.
    """

    def __init__(self, data):
        self._event_id    = data["about"]["eventIdx"]
        self._description = data["result"]["description"]
        self._period      = data["about"]["period"]
        self._time        = data["about"]["periodTimeRemaining"]
        self._home_goals  = data["about"]["goals"]["home"]
        self._away_goals  = data["about"]["goals"]["away"]

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.event_id == other.event_id

    @property
    def event_id(self):
        """Getter for the event ID."""
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Setter for the event ID."""
        self._event_id = event_id

    @property
    def description(self):
        """Getter for the description."""
        return self._description

    @description.setter
    def description(self, description):
        """Setter for the description."""
        self._description = description

    @property
    def period(self):
        """Getter for the period."""
        return self._period

    @period.setter
    def period(self, period):
        """Setter for the period."""
        self._period = period

    @property
    def time(self):
        """Getter for the time."""
        return self._time

    @time.setter
    def time(self, time):
        """Setter for the time."""
        self._time = time

    @property
    def home_goals(self):
        """Getter for the home goals."""
        return self._home_goals

    @home_goals.setter
    def home_goals(self, home_goals):
        """Setter for the home goals."""
        self._home_goals = home_goals

    @property
    def away_goals(self):
        """Getter for the away goals."""
        return self._away_goals

    @away_goals.setter
    def away_goals(self, away_goals):
        """Setter for the away goals."""
        self._away_goals = away_goals


class BlockedShot(Event):
    """
    Description:
        The Blocked Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._shooter = get_player_name(data, "Shooter")
        self._blocker = get_player_name(data, "Blocker")

    def __str__(self):
        return str(self.event_id) + " = Blocked Shot - " + self.description

    @property
    def shooter(self):
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def blocker(self):
        """Getter for the blocker."""
        return self._blocker

    @blocker.setter
    def blocker(self, blocker):
        """Setter for the blocker."""
        self._blocker = blocker


class Challenge(Event):
    """
    Description:
        The Challenge event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._team = get_team(data)

    def __str__(self):
        return str(self.event_id) + " = Official Challenge - " + self.description

    @property
    def team(self):
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team):
        """Setter for the team."""
        self._team = team


class Faceoff(Event):
    """
    Description:
        The Faceoff event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._winner = get_player_name(data, "Winner")
        self._loser  = get_player_name(data, "Loser")

    def __str__(self):
        return str(self.event_id) + " = Faceoff - " + self.description

    @property
    def winner(self):
        """Getter for the winner."""
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Setter for the winner."""
        self._winner = winner

    @property
    def loser(self):
        """Getter for the loser."""
        return self._loser

    @loser.setter
    def loser(self, loser):
        """Setter for the loser."""
        self._loser = loser


class GameEnd(Event):
    """
    Description:
        The Game End event.
    """

    def __str__(self):
        return str(self.event_id) + " = Game End - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__


class GameOfficial(Event):
    """
    Description:
        The Game Official event.
    """

    def __str__(self):
        return str(self.event_id) + " = Game Official - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__


class GameScheduled(Event):
    """
    Description:
        The Game Scheduled event.
    """

    def __str__(self):
        return str(self.event_id) + " = Game Scheduled - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__


class Giveaway(Event):
    """
    Description:
        The Giveaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._player = get_player_name(data, "PlayerID")

    def __str__(self):
        return str(self.event_id) + " = Giveaway - " + self.description

    @property
    def player(self):
        """Getter for the player."""
        return self._player

    @player.setter
    def player(self, player):
        """Setter for the player."""
        self._player = player


class Goal(Event):
    """
    Description:
        The Goal event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._team             = get_team(data)
        self._scorer           = get_player_name(data, "Scorer")
        self._primary_assist   = get_player_name(data, "Assist", 1)
        self._secondary_assist = get_player_name(data, "Assist", 2)
        self._goalie           = get_player_name(data, "Goalie")
        self._strength         = get_value(data, "result", "strength", "code")
        self._is_empty_net     = get_value(data, "result", "emptyNet")

    def __str__(self):
        return str(self.event_id) + " = Goal - " + self.description

    def __eq__(self, other):
        return (self.__class__        == other.__class__ and
                self.event_id         == other.event_id and
                self.scorer           == other.scorer and
                self.primary_assist   == other.primary_assist and
                self.secondary_assist == other.secondary_assist and
                self.time             == other.time)

    @property
    def team(self):
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team):
        """Setter for the team."""
        self._team = team

    @property
    def scorer(self):
        """Getter for the scorer."""
        return self._scorer

    @scorer.setter
    def scorer(self, scorer):
        """Setter for the scorer."""
        self._scorer = scorer

    @property
    def primary_assist(self):
        """Getter for the primary assist."""
        return self._primary_assist

    @primary_assist.setter
    def primary_assist(self, primary_assist):
        """Setter for the primary assist."""
        self._primary_assist = primary_assist

    @property
    def secondary_assist(self):
        """Getter for the secondary assist."""
        return self._secondary_assist

    @secondary_assist.setter
    def secondary_assist(self, secondary_assist):
        """Setter for the secondary assist."""
        self._secondary_assist = secondary_assist

    @property
    def goalie(self):
        """Getter for the goalie."""
        return self._goalie

    @goalie.setter
    def goalie(self, goalie):
        """Setter for the goalie."""
        self._goalie = goalie

    @property
    def strength(self):
        """Getter for the strength."""
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Setter for the strength."""
        self._strength = strength

    @property
    def is_empty_net(self):
        """Getter for the is_empty_net property."""
        return self._is_empty_net

    @is_empty_net.setter
    def is_empty_net(self, is_empty_net):
        """Setter for the is_empty_net property."""
        self._is_empty_net = is_empty_net


class Hit(Event):
    """
    Description:
        The Hit event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._hitter = get_player_name(data, "Hitter")
        self._hittee = get_player_name(data, "Hittee")

    def __str__(self):
        return str(self.event_id) + " = Hit - " + self.description

    @property
    def hitter(self):
        """Getter for the hitter."""
        return self._hitter

    @hitter.setter
    def hitter(self, hitter):
        """Setter for the hitter."""
        self._hitter = hitter

    @property
    def hittee(self):
        """Getter for the hittee."""
        return self._hittee

    @hittee.setter
    def hittee(self, hittee):
        """Setter for the hittee."""
        self._hittee = hittee


class MissedShot(Event):
    """
    Description:
        The Missed Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self._shooter = get_player_name(data, "Shooter")
        self._goalie  = get_player_name(data, "Unknown")

    def __str__(self):
        return str(self.event_id) + " = Missed Shot - " + self.description

    @property
    def shooter(self):
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def goalie(self):
        """Getter for the goalie."""
        return self._goalie

    @goalie.setter
    def goalie(self, goalie):
        """Setter for the goalie."""
        self._goalie = goalie


class Penalty(Event):
    """
    Description:
        The Penalty event.
    """

    def __init__(self, data):

        super().__init__(data)

        reason   = get_value(data, "result", "secondaryType")
        severity = get_value(data, "result", "penaltySeverity")

        self._taker    = get_player_name(data, "PenaltyOn")
        self._drawn_by = get_player_name(data, "DrewBy")
        self._reason   = None if reason is None else reason.lower()
        self._severity = None if severity is None else severity.lower()
        self._minutes  = get_value(data, "result", "penaltyMinutes")
        self._team     = get_team(data)

        if self._reason == "minor":
            self._reason = None


    def __str__(self):
        return str(self.event_id) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.event_id  == other.event_id and
                self.taker     == other.taker and
                self.drawn_by  == other.drawn_by and
                self.reason    == other.reason and
                self.severity  == other.severity and
                self.minutes   == other.minutes)

    @property
    def taker(self):
        """Getter for the taker."""
        return self._taker

    @taker.setter
    def taker(self, taker):
        """Setter for the taker."""
        self._taker = taker

    @property
    def drawn_by(self):
        """Getter for the drawn_by property."""
        return self._drawn_by

    @drawn_by.setter
    def drawn_by(self, drawn_by):
        """Setter for the _drawn_by property."""
        self._taker = drawn_by

    @property
    def reason(self):
        """Getter for the reason."""
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Setter for the reason."""
        self._reason = reason

    @property
    def severity(self):
        """Getter for the severity."""
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Setter for the severity."""
        self._severity = severity

    @property
    def minutes(self):
        """Getter for the minutes."""
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Setter for the minutes."""
        self._minutes = minutes

    @property
    def team(self):
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team):
        """Setter for the team."""
        self._team = team


class PenaltyShot(Event):
    """
    Description:
        The Penalty Shot event.
    """

    def __init__(self, data):
        super().__init__(data)

        reason   = get_value(data, "result", "secondaryType")
        severity = get_value(data, "result", "penaltySeverity")

        self._taker    = get_player_name(data, "PenaltyOn")
        self._drawn_by = get_player_name(data, "DrewBy")
        self._reason   = None if reason is None else reason.lower().replace("ps - ", "")
        self._severity = None if severity is None else severity.lower()
        self._minutes  = get_value(data, "result", "penaltyMinutes")
        self._team     = get_team(data)

    def __str__(self):
        return str(self.event_id) + " = Penalty - " + self.description

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.event_id  == other.event_id and
                self.taker     == other.taker and
                self.drawn_by  == other.drawn_by and
                self.reason    == other.reason and
                self.severity  == other.severity and
                self.minutes   == other.minutes)

    @property
    def taker(self):
        """Getter for the taker."""
        return self._taker

    @taker.setter
    def taker(self, taker):
        """Setter for the taker."""
        self._taker = taker

    @property
    def drawn_by(self):
        """Getter for the drawn_by property."""
        return self._drawn_by

    @drawn_by.setter
    def drawn_by(self, drawn_by):
        """Setter for the _drawn_by property."""
        self._taker = drawn_by

    @property
    def reason(self):
        """Getter for the reason."""
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Setter for the reason."""
        self._reason = reason

    @property
    def severity(self):
        """Getter for the severity."""
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Setter for the severity."""
        self._severity = severity

    @property
    def minutes(self):
        """Getter for the minutes."""
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Setter for the minutes."""
        self._minutes = minutes

    @property
    def team(self):
        """Getter for the team."""
        return self._team

    @team.setter
    def team(self, team):
        """Setter for the team."""
        self._team = team


class PeriodEnd(Event):
    """
    Description:
        The Period End event.
    """

    def __str__(self):
        return str(self.event_id) + " = Period End - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class PeriodOfficial(Event):
    """
    Description:
        The Period Official event.
    """

    def __str__(self):
        return str(self.event_id) + " = Period Official - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class PeriodReady(Event):
    """
    Description:
        The Period Ready event.
    """

    def __str__(self):
        return str(self.event_id) + " = Period Ready - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class PeriodStart(Event):
    """
    Description:
        The Period Start event.
    """

    def __str__(self):
        return str(self.event_id) + " = Period Start - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class Shot(Event):
    """
    Description:
        The Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.shooter = get_player_name(data, "Shooter")
        self.goalie  = get_player_name(data, "Goalie")

    def __str__(self):
        return str(self.event_id) + " = Shot - " + self.description

    @property
    def shooter(self):
        """Getter for the shooter."""
        return self._shooter

    @shooter.setter
    def shooter(self, shooter):
        """Setter for the shooter."""
        self._shooter = shooter

    @property
    def goalie(self):
        """Getter for the goalie."""
        return self._goalie

    @goalie.setter
    def goalie(self, goalie):
        """Setter for the goalie."""
        self._goalie = goalie


class Stoppage(Event):
    """
    Description:
        The Stoppage event.
    """

    def __str__(self):
        return str(self.event_id) + " = Stoppage - " + self.description


class Takeaway(Event):
    """
    Description:
        The Takeaway event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.player = get_player_name(data, "PlayerID")

    def __str__(self):
        return str(self.event_id) + " = Takeaway - " + self.description


event_constructors = {
    Events.BLOCKED_SHOT_EVENT:    BlockedShot,
    Events.CHALLENGE_EVENT:       Challenge,
    Events.FACEOFF_EVENT:         Faceoff,
    Events.GAME_END_EVENT:        GameEnd,
    Events.GAME_OFFICIAL_EVENT:   GameOfficial,
    Events.GAME_SCHEDULED_EVENT:  GameScheduled,
    Events.GIVEAWAY_EVENT:        Giveaway,
    Events.GOAL_EVENT:            Goal,
    Events.HIT_EVENT:             Hit,
    Events.MISSED_SHOT_EVENT:     MissedShot,
    Events.PENALTY_EVENT:         Penalty,
    Events.PENALTY_SHOT_EVENT:    PenaltyShot,
    Events.PERIOD_END_EVENT:      PeriodEnd,
    Events.PERIOD_OFFICIAL_EVENT: PeriodOfficial,
    Events.PERIOD_READY_EVENT:    PeriodReady,
    Events.PERIOD_START_EVENT:    PeriodStart,
    Events.SHOT_EVENT:            Shot,
    Events.STOPPAGE_EVENT:        Stoppage,
    Events.TAKEAWAY_EVENT:        Takeaway
}

def to_event(data):
    """
    Description:
        This function is used to construct events from JSON data.
    """
    try:
        is_penalty = data["result"]["event"] == "Penalty"
        if is_penalty and data["result"]["penaltySeverity"] == "Penalty Shot":
            event_type = Events.PENALTY_SHOT_EVENT
        else:
            event_type = Events(data["result"]["event"])

    except ValueError:
        logger.log_error("An unknown event type was processed: " + data["result"]["event"])

    return event_constructors[event_type](data)

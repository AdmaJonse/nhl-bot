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
            value = data.get(key, "")
            data = value
        except KeyError:
            logger.log_error("Could not find key: " + key)
            return ""
        except AttributeError:
            logger.log_error("Could not find key: " + key)
            return ""
    return value


class Event:
    """
    Description:
        The base event class.
    """

    def __init__(self, data):
        self.event_id    = data["about"]["eventIdx"]
        self.description = data["result"]["description"]
        self.period      = data["about"]["period"]
        self.time        = data["about"]["periodTimeRemaining"]
        self.home_goals  = data["about"]["goals"]["home"]
        self.away_goals  = data["about"]["goals"]["away"]

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.event_id == other.event_id


class BlockedShot(Event):
    """
    Description:
        The Blocked Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.shooter = get_player_name(data, "Shooter")
        self.blocker = get_player_name(data, "Blocker")

    def __str__(self):
        return str(self.event_id) + " = Blocked Shot - " + self.description


class Challenge(Event):
    """
    Description:
        The Challenge event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.team = get_team(data)

    def __str__(self):
        return str(self.event_id) + " = Official Challenge - " + self.description


class Faceoff(Event):
    """
    Description:
        The Faceoff event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.winner = get_player_name(data, "Winner")
        self.loser  = get_player_name(data, "Loser")

    def __str__(self):
        return str(self.event_id) + " = Faceoff - " + self.description


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
        self.player = get_player_name(data, "PlayerID")

    def __str__(self):
        return str(self.event_id) + " = Giveaway - " + self.description


class Goal(Event):
    """
    Description:
        The Goal event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.team             = get_team(data)
        self.scorer           = get_player_name(data, "Scorer")
        self.primary_assist   = get_player_name(data, "Assist", 1)
        self.secondary_assist = get_player_name(data, "Assist", 2)
        self.goalie           = get_player_name(data, "Goalie")
        self.strength         = get_value(data, "result", "strength", "code")
        self.is_empty_net     = get_value(data, "result", "emptyNet")

    def __str__(self):
        return str(self.event_id) + " = Goal - " + self.description

    def __eq__(self, other):
        return (self.__class__        == other.__class__ and
                self.event_id         == other.event_id and
                self.scorer           == other.scorer and
                self.primary_assist   == other.primary_assist and
                self.secondary_assist == other.secondary_assist and
                self.time             == other.time)


class Hit(Event):
    """
    Description:
        The Hit event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.hitter = get_player_name(data, "Hitter")
        self.hittee = get_player_name(data, "Hittee")

    def __str__(self):
        return str(self.event_id) + " = Hit - " + self.description


class MissedShot(Event):
    """
    Description:
        The Missed Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.shooter = get_player_name(data, "Shooter")
        self.goalie  = get_player_name(data, "Unknown")

    def __str__(self):
        return str(self.event_id) + " = Missed Shot - " + self.description


class Penalty(Event):
    """
    Description:
        The Penalty event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.taker    = get_player_name(data, "PenaltyOn")
        self.drawn_by = get_player_name(data, "DrewBy")
        self.reason   = get_value(data, "result", "secondaryType").lower()
        self.severity = get_value(data, "result", "penaltySeverity").lower()
        self.minutes  = get_value(data, "result", "penaltyMinutes")
        self.team     = get_team(data)

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


class PenaltyShot(Event):
    """
    Description:
        The Penalty Shot event.
    """

    def __init__(self, data):
        super().__init__(data)
        self.taker    = get_player_name(data, "PenaltyOn")
        self.drawn_by = get_player_name(data, "DrewBy")
        self.reason   = get_value(data, "result", "secondaryType").lower().replace("ps - ", "")
        self.severity = get_value(data, "result", "penaltySeverity").lower()
        self.minutes  = get_value(data, "result", "penaltyMinutes")
        self.team     = get_team(data)

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
        TODO
    """

    def __str__(self):
        return str(self.event_id) + " = Period Official - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class PeriodReady(Event):
    """
    Description:
        TODO
    """

    def __str__(self):
        return str(self.event_id) + " = Period Ready - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class PeriodStart(Event):
    """
    Description:
        TODO
    """

    def __str__(self):
        return str(self.event_id) + " = Period Start - " + self.description

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.period == other.period


class Shot(Event):
    """
    Description:
        TODO
    """

    def __init__(self, data):
        super().__init__(data)
        self.shooter = get_player_name(data, "Shooter")
        self.goalie  = get_player_name(data, "Goalie")

    def __str__(self):
        return str(self.event_id) + " = Shot - " + self.description


class Stoppage(Event):
    """
    Description:
        TODO
    """

    def __str__(self):
        return str(self.event_id) + " = Stoppage - " + self.description


class Takeaway(Event):
    """
    Description:
        TODO
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
        TODO
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

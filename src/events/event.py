"""
This module defines event classes. Event data is parsed from the
NHL API JSON data and converted into Event objects.

The main benefit of an object-based approach rather than simply
comparing the JSON data itself, is that it makes comparisons
between events far simpler. We have more control over the
comparisons themselves and we're no longer going to trigger event
update processing when minor JSON fields change as opposed to
relevant event data.
"""

from datetime import datetime
from typing import Any, Optional
from dateutil import parser

from src.exceptions import InsufficientData
from src.logger import log
from src.data.game_data import GameData
from src.data.period import Period
from src.data.score import Score
from src.data.line_score import LineScore
from src.utils import pad_blob, pad_code


def get_player_name(event : Any, player_type : str, index : int = 1):
    """
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


def get_team(event : Any):
    """
    Return the name of the team in the given event. Log an error
    and return None if no team was found.
    """
    try:
        return event["team"]["name"]
    except KeyError:
        log.info("Could not find team.")
        return None


def get_value(data : Any, *args):
    """
    Helper function for retrieving values from multi-level dictionaries.
    If the key is not found, return an empty string.
    """
    for key in args:
        try:
            value = data.get(key)
            data = value
        except KeyError:
            log.error("Could not find key: " + key)
            return None
        except AttributeError:
            log.error("Could not find key: " + key)
            return None
    return value


class Event:
    """
    The base event class.
    """

    null_post = None

    def __init__(self, data : Any):
        self._tweet_id    : Optional[int] = None
        self._event_id    : int           = int(data["about"]["eventId"])
        self._description : str           = data["result"]["description"]
        self._period      : Period        = Period(data["about"])
        self._time        : str           = data["about"]["periodTimeRemaining"]
        self._timestamp   : datetime      = parser.parse(data["about"]["dateTime"])
        self._score       : Score         = Score(data["about"])
        self._auto_reply  : bool          = False

        if self.description is None:
            raise InsufficientData

        if self.period is None:
            raise InsufficientData

        if self.time is None:
            raise InsufficientData

        if self.timestamp is None:
            raise InsufficientData


    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.period.number == other.period.number and
                self.time == other.time)

    @property
    def code(self) -> str:
        """
        Return a four letter code representing the event type.
        """
        code : str = "EVENT"
        return pad_code(code)


    @property
    def blob(self) -> str:
        """
        Return a unique identifier for this event that will not change, even if the event_id int
        changes.
        """

        blob : str = "######"
        return pad_blob(blob)


    @property
    def id(self) -> str:
        """
        Return a unique identifier for this event that will not change, even if the event_id int
        changes.
        """

        name        : str = self.code
        time        : str = str(self.period.number) + "-" + str(self.time).replace(':', '')
        description : str = self.blob
        return name + "-" + time + "-" + description


    @property
    def tweet_id(self) -> Optional[int]:
        """
        Getter for the tweet ID.
        """
        return self._tweet_id


    @tweet_id.setter
    def tweet_id(self, tweet_id : Optional[int]):
        """
        Setter for the tweet ID.
        """
        self._tweet_id = tweet_id


    @property
    def event_id(self) -> Optional[int]:
        """
        Getter for the NHL API's Event ID.
        """
        return self._event_id


    @property
    def has_tweeted(self) -> bool:
        """
        Return a boolean indicating whether or not a tweet has been sent for this event.
        """
        return self._tweet_id is not None and self._tweet_id > 0


    @property
    def description(self) -> Optional[str]:
        """
        Getter for the description.
        """
        return self._description


    @description.setter
    def description(self, description : str):
        """
        Setter for the description.
        """
        self._description = description


    @property
    def period(self) -> Period:
        """
        Getter for the period.
        """
        return self._period


    @period.setter
    def period(self, period : Period):
        """
        Setter for the period.
        """
        self._period = period


    @property
    def time(self) -> Optional[str]:
        """
        Getter for the time.
        """
        return self._time


    @time.setter
    def time(self, time : str):
        """
        Setter for the time.
        """
        self._time = time


    @property
    def timestamp(self) -> datetime:
        """
        Getter for the time.
        """
        return self._timestamp


    @timestamp.setter
    def timestamp(self, timestamp : datetime):
        """
        Setter for the timestamp.
        """
        self._timestamp = timestamp


    @property
    def score(self) -> Score:
        """
        Getter for the score.
        """
        return self._score


    def get_post(self, _game_data : GameData, _line_score : LineScore) -> Optional[str]:
        """
        The base implementation for returning post text. This implementation simply
        returns None and will not result in any tweet being posted.
        """
        return self.null_post


    def get_reply(self, _game : GameData, _line : LineScore, _previous : 'Event') -> Optional[str]:
        """
        The base implementation for returning reply text. This implementation simply
        returns None and will not result in any tweet being posted.
        """
        return self.null_post

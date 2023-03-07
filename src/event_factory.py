"""
This module defines the factory for Event objects. Given JSON data defining the event, we will
determine the event type and dispatch to constructor of the expected Event subclass.
"""

from typing import Dict, Optional, Type
from enum import Enum

from src.logger import log
from src.events.event import Event
from src.events.blocked_shot import BlockedShot
from src.events.challenge import Challenge
from src.events.faceoff import Faceoff
from src.events.failed_shot import FailedShot
from src.events.game_end import GameEnd
from src.events.game_official import GameOfficial
from src.events.game_scheduled import GameScheduled
from src.events.giveaway import Giveaway
from src.events.goal import Goal
from src.events.hit import Hit
from src.events.missed_shot import MissedShot
from src.events.penalty import Penalty
from src.events.penalty_shot import PenaltyShot
from src.events.period_end import PeriodEnd
from src.events.period_official import PeriodOfficial
from src.events.period_ready import PeriodReady
from src.events.period_start import PeriodStart
from src.events.ping import Ping
from src.events.shot import Shot
from src.events.shootout_end import ShootoutEnd
from src.events.stoppage import Stoppage
from src.events.takeaway import Takeaway
from src.exceptions import InsufficientData

class Events(Enum):
    """
    The event type enumeration.
    """
    BLOCKED_SHOT_EVENT    = "Blocked Shot"
    CHALLENGE_EVENT       = "Official Challenge"
    FACEOFF_EVENT         = "Faceoff"
    FAILED_SHOT_EVENT     = "Failed Shot Attempt"
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
    PING_EVENT            = "Ping"
    SHOT_EVENT            = "Shot"
    SHOOTOUT_END_EVENT    = "Shootout Complete"
    STOPPAGE_EVENT        = "Stoppage"
    TAKEAWAY_EVENT        = "Takeaway"

event_constructors : Dict[Events, Type[Event]] = {
    Events.BLOCKED_SHOT_EVENT:    BlockedShot,
    Events.CHALLENGE_EVENT:       Challenge,
    Events.FACEOFF_EVENT:         Faceoff,
    Events.FAILED_SHOT_EVENT:     FailedShot,
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
    Events.PING_EVENT:            Ping,
    Events.SHOT_EVENT:            Shot,
    Events.SHOOTOUT_END_EVENT:    ShootoutEnd,
    Events.STOPPAGE_EVENT:        Stoppage,
    Events.TAKEAWAY_EVENT:        Takeaway
}

def create(data) -> Optional[Event]:
    """
    This function is used to construct events from JSON data.
    """
    try:

        is_penalty     : bool = data["result"]["event"] == Events.PENALTY_EVENT.value
        is_missed_shot : bool = data["result"]["event"] == Events.MISSED_SHOT_EVENT.value

        if is_penalty and data["result"]["penaltySeverity"] == Events.PENALTY_SHOT_EVENT.value:
            event_type = Events.PENALTY_SHOT_EVENT
        elif is_missed_shot and "goalpost" in data["result"]["description"].lower():
            event_type = Events.PING_EVENT
        elif is_missed_shot and "crossbar" in data["result"]["description"].lower():
            event_type = Events.PING_EVENT
        else:
            event_type = Events(data["result"]["event"])

    except ValueError:
        log.error("An unknown event type was processed: " + data["result"]["event"])

    try:
        return event_constructors[event_type](data)
    except InsufficientData:
        return None

"""
This module contains the data class that defines a power play.
"""

from dataclasses import dataclass
import time
from typing import Optional

from src.logger import log

@dataclass
class PowerPlay:
    """
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
    Create a power play object using line score data.
    """

    strength        : str  = data["powerPlayStrength"]
    home_skaters    : int  = data["teams"]["home"]["numSkaters"]
    home_power_play : bool = data["teams"]["home"]["powerPlay"]
    away_skaters    : int  = data["teams"]["away"]["numSkaters"]
    away_power_play : bool = data["teams"]["away"]["powerPlay"]

    try:

        time_remaining  : int  = data["powerPlayInfo"]["situationTimeRemaining"]
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
            log.error("Line score indicates home powerplay, but skater counts are wrong.")
            log.error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "home"

    elif away_power_play:

        if home_skaters >= away_skaters:
            log.error("Line score indicates away powerplay, but skater counts are wrong.")
            log.error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "away"

    else:

        if home_skaters != away_skaters:
            log.error("Line score indicates even strength, but skater counts are wrong.")
            log.error("  Home: " + str(home_skaters) + ", Away: "+ str(away_skaters))

        team = "even"

    return PowerPlay (
        team           = team,
        home_skaters   = home_skaters,
        away_skaters   = away_skaters,
        strength       = strength,
        time_remaining = time.strftime("%M:%S", time.gmtime(time_remaining)),
        time_elapsed   = time.strftime("%M:%S", time.gmtime(time_elapsed))
    )

"""
This module contains the data class for a shootout event.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class ShootoutData:
    """
    This data class defines data for a shootout event.
    """
    home_goals    : int = 0
    home_attempts : int = 0
    away_goals    : int = 0
    away_attempts : int = 0


def get_shootout(data) -> Optional[ShootoutData]:
    """
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

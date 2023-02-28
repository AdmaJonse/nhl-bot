"""
This module contains the dataclass defining data that is specific to one team.
"""
from dataclasses import dataclass

@dataclass
class TeamData:
    """
    This data class defines data that is specific to one team.
    """
    shots          : int  = 0
    goals          : int  = 0
    goalie_pulled  : bool = False
    skater_count   : int  = 0
    is_power_play  : bool = False

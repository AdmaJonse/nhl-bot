"""
Description:
    This module defines templates for game event tweets. These templates
    contain placeholders for variables that will be defined in the calling
    code.
"""

#################################################
# Game End
#################################################

GAME_END_TEMPLATE = """
The game is over. {winner} wins!

Final Score:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""


#################################################
# Period Start
#################################################

PERIOD_START_TEMPLATE = """
{period} is starting at {venue} in {city}.

{hashtags}
"""


#################################################
# Period End
#################################################

PERIOD_END_TEMPLATE = """
{period} is over at {venue}.

Goals
{home_team}: {home_goals}
{away_team}: {away_goals}

Shots on Goal
{home_team}: {home_shots}
{away_team}: {away_shots}

{hashtags}
"""


#################################################
# Shot on Goal
#################################################
SHOT_TEMPLATE = """
Shot on goal by {team}.

{description}

Shots On Goal:
{home_team}: {home_shots}
{away_team}: {away_shots}

{hashtags}
"""


#################################################
# Penalty
#################################################
PENALTY_TEMPLATE = """
There is a penalty on {team}.

{player}
{minutes} minute {severity} for {penalty}

{hashtags}
"""

PENALTY_SHOT_TEMPLATE = """
That's a penalty shot for {team}!

The infraction is against {player} for {penalty}.

{hashtags}
"""

PENALTY_REPLY_TEMPLATE = """
There has been an update to the penalty on {team}.

{player}
{minutes} minute {severity} for {penalty}

{hashtags}
"""


#################################################
# Goal
#################################################

GOAL_TEMPLATE = """
{team} goal!

Scored by {player} with {time} remaining in the {period} period.

{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

GOAL_REPLY_TEMPLATE = """
There has been update to the {team} goal scored with {time} remaining in the {period} period.

{description}

{hashtags}
"""


#################################################
# Coach's Challenge
#################################################

CHALLENGE_TEMPLATE = """
{team} is challenging the ruling on the play.

{hashtags}
"""

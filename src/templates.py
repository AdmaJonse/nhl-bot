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
{period} is over at {venue} in {city}.

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
# Ping!
#################################################
PING_TEMPLATE = """
Ping!

{shooter}'s shot on {goalie} hit the {goal_post}.

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

Scored by {scorer} with {time} remaining in the {period} period.
"""

POWER_PLAY_GOAL_TEMPLATE = """
Power play goal for {team}!

Scored by {scorer} with {time} remaining in the {period} period.
"""

SHORT_HANDED_GOAL_TEMPLATE = """
Short-handed goal for {team}!

Scored by {scorer} with {time} remaining in the {period} period.
"""

EMPTY_NET_GOAL_TEMPLATE = """
Empty net goal for {team}!

Scored by {scorer} with {time} remaining in the {period} period.
"""

GOAL_FOOTER_TEMPLATE = """
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

ONE_ASSIST_TEMPLATE = """
Assisted by {primary_assist}.
"""

TWO_ASSIST_TEMPLATE = """
Assisted by {primary_assist} and {secondary_assist}.
"""

GOAL_REPLY_TEMPLATE = """
There has been update to the {team} goal scored with {time} remaining in the {period} period.

{description}

{hashtags}
"""

SCORER_UPDATE_TEMPLATE = """
The goal is now being awarded to {scorer}.

{hashtags}
"""

ASSIST_ADD_PRIMARY_TEMPLATE = """
A primary assist has been awarded to {primary_assist}.

{hashtags}
"""

ASSIST_ADD_SECONDARY_TEMPLATE = """
A secondary assist has been awarded to {secondary_assist}.

{hashtags}
"""

ASSIST_ADD_BOTH_TEMPLATE = """
Assists have been awarded to {primary_assist} and {secondary_assist}.

{hashtags}
"""

ASSIST_UPDATE_TEMPLATE = """
The assists have been changed on this goal. Assists are now awarded to {primary_assist} and {secondary_assist}.

{hashtags}
"""

PRIMARY_ASSIST_UPDATE_TEMPLATE = """
The assists have been changed on this goal. The primary assist has been awarded to {primary_assist}.

{hashtags}
"""

SECONDARY_ASSIST_UPDATE_TEMPLATE = """
The assists have been changed on this goal. The secondary assist has been awarded to {secondary_assist}.

{hashtags}
"""

GOAL_TIME_UPDATE_TEMPLATE = """
The time of this goal has been changed. The scoresheet now indicates this goal occurred with {time} remaining in the {period} period.

{hashtags}
"""


#################################################
# Coach's Challenge
#################################################

CHALLENGE_TEMPLATE = """
{team} is challenging the ruling on the play.

{hashtags}
"""

"""
This module defines templates for game event tweets. These templates
    contain placeholders for variables that will be defined in the calling
    code.
"""

#################################################
# Game Day
#################################################

GAME_DAY_TEMPLATE = """
It's game day!

{home_team} takes on {away_team} at {venue}. The puck drops at {time}.

{hashtags}
"""

#################################################
# Game End
#################################################

GAME_END_TEMPLATE = """
The game is over. {winner} wins!

Final:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

GAME_END_OT_TEMPLATE = """
The game is over. {winner} wins!

Final/OT:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

GAME_END_SO_TEMPLATE = """
The game is over. {winner} wins!

Final/SO:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""


#################################################
# Period Start
#################################################

PERIOD_START_TEMPLATE = """
{period} is starting at {venue}.

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
# Shootout
#################################################

SHOOTOUT_MISS_TEMPLATE = """
{team} miss.

The shootout attempt by {shooter} failed.

{hashtags}
"""

SHOOTOUT_SAVE_TEMPLATE = """
{team} miss.

{goalie} stopped the shootout attempt by {shooter}.

{hashtags}
"""

SHOOTOUT_GOAL_TEMPLATE = """
{team} goal!

{scorer} scores against {goalie} in the shootout.

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
There is a penalty on {penalized_team}.

{player} will serve a {minutes} minute {severity} for {penalty}.

{hashtags}
"""

HOME_POWER_PLAY_TEMPLATE = """
{home_team} will have a {home_skaters}-on-{away_skaters} power play for {time_remaining}.

{hashtags}
"""

AWAY_POWER_PLAY_TEMPLATE = """
{away_team} will have a {away_skaters}-on-{home_skaters} power play for {time_remaining}.

{hashtags}
"""

EVEN_STRENGTH_TEMPLATE = """
The teams will play {home_skaters}-on-{away_skaters} for {time_remaining}.

{hashtags}
"""

PENALTY_SHOT_TEMPLATE = """
That's a penalty shot for {team}!

The infraction is against {player} for {penalty}.

{hashtags}
"""

PENALTY_REPLY_TEMPLATE = """
There has been an update to the penalty on {team}.

{player} will serve a {minutes} minute {severity} for {penalty}

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

#################################################
# Highlights
#################################################

HIGHLIGHT_TEMPLATE = """
{description}. 

{hashtags}
"""

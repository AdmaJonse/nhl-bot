#################################################
# Game End
#################################################

game_end_template = """
The game is over. {winner} wins!

Final Score:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""


#################################################
# Period Start
#################################################

period_start_template = """
{period} is starting at {venue} in {city}.

{hashtags}
"""


#################################################
# Period End
#################################################

period_end_template = """
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
shot_template = """
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
penalty_template = """
There is a penalty on {team}.

{player}
{minutes} minute {severity} for {penalty}

{hashtags}
"""

penalty_shot_template = """
That's a penalty shot for {team}!

The infraction is against {player} for {penalty}.

{hashtags}
"""

penalty_reply_template = """
There has been an update to the penalty on {team}.

{player}
{minutes} minute {severity} for {penalty}

{hashtags}
"""


#################################################
# Goal
#################################################

goal_template = """
{team} goal!

Scored by {player} with {time} remaining in the {period} period.

{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

goal_reply_template = """
There has been update to the {team} goal scored with {time} remaining in the {period} period.

{description}

{hashtags}
"""


#################################################
# Coach's Challenge
#################################################

challenge_template = """
{team} is challenging the ruling on the play.

{hashtags}
"""


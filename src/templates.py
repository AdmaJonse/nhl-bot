#################################################
# Game End
#################################################

game_end_template = """
The game is over. {winner} wins.

Final Score:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""


#################################################
# Period Start
#################################################

period_start_template = """
{period} is starting at {venue}.

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


#################################################
# Goal
#################################################

goal_template = """
{team} goal! 

Scored by {player} with {time} remaing in the {period} period.

Goals
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""


#################################################
# Coach's Challenge
#################################################

challenge_template = """
{team} is challenging the ruling on the play.

{hashtags}
"""


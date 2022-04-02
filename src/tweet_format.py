game_end_string = """
The game is over. {winner} wins.

Final Score:
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

shot_string = """
Shot on goal by {team}.

{description}

Shots On Goal:
{home_team}: {home_shots}
{away_team}: {away_shots}

{hashtags}
"""

penalty_string = """
There is a penalty on {team}.

{player}
{minutes} minute {severity} for {penalty}

{hashtags}
"""

period_start_string = """
{period} is starting at {venue}.

{hashtags}
"""

period_end_string = """
{period} is over at {venue}.

Goals
{home_team}: {home_goals}
{away_team}: {away_goals}

Shots on Goal
{home_team}: {home_shots}
{away_team}: {away_shots}

{hashtags}
"""

goal_string = """
{team} goal! 

Scored by {player} with {time} remaing in the {period} period.

Goals
{home_team}: {home_goals}
{away_team}: {away_goals}

{hashtags}
"""

challenge_string = """
{team} is challenging the ruling on the play.

{hashtags}
"""
import tweeter

blocked_shot_event    = "Blocked Shot"
challenge_event       = "Official Challenge"
faceoff_event         = "Faceoff"
game_end_event        = "Game End"
game_official_event   = "Game Official"
game_scheduled_event  = "Game Scheduled"
giveaway_event        = "Giveaway" 
goal_event            = "Goal"
hit_event             = "Hit" 
missed_shot_event     = "Missed Shot"
penalty_event         = "Penalty" 
period_end_event      = "Period End"
period_official_event = "Period Official"
period_ready_event    = "Period Ready"
period_start_event    = "Period Start"
shot_event            = "Shot"
stoppage_event        = "Stoppage" 
takeaway_event        = "Takeaway"


def get_timestamp(data):
    return data["about"]["dateTime"]


def get_description(data):
    return data["result"]["description"]


def get_home_goals(data):
    return data["about"]["goals"]["home"]


def get_away_goals(data):
    return data["about"]["goals"]["away"]
    
    
def get_home_shots(data):
    return data["teams"]["home"]["shotsOnGoal"]


def get_away_shots(data):
    return data["teams"]["away"]["shotsOnGoal"]


def get_period(data):
    return data["about"]["goals"]["away"]


def get_player_name(data):
    return data["players"][0]["fullName"]


class Printer:

    def get_game_data(self, data):
        self.home_location = data["teams"]["home"]["locationName"]
        self.home_team = data["teams"]["home"]["teamName"]
        self.home_abbreviation = data["teams"]["home"]["abbreviation"]
        self.home_full_name = data["teams"]["home"]["name"]
        self.away_location = data["teams"]["away"]["locationName"]
        self.away_team = data["teams"]["away"]["teamName"]
        self.away_abbreviation = data["teams"]["away"]["abbreviation"]
        self.away_full_name = data["teams"]["away"]["name"]
        self.date = data["datetime"]["dateTime"]
        self.venue = data["teams"]["home"]["venue"]["name"]
        self.is_home = self.home_location == "Colorado"
        self.team_hashtag = "#GoAvsGo"
        self.game_hashtag = "#" + self.away_abbreviation + "vs" + self.home_abbreviation


    def update_line_score(self, line_score):
        self.line_score = line_score


    def __init__(self, data):
        self.tweeter = tweeter.Tweeter()
        self.game_data = data["gameData"]
        self.line_score = data["liveData"]["linescore"]        
        self.get_game_data(self.game_data)
        self.print_constants()
   

    #################################################################
    #  Helper Functions
    #################################################################

    def print_constants(self):
        print("Home Location:     " + self.home_location)
        print("Home Team:         " + self.home_team)
        print("Home Abbreviation: " + self.home_abbreviation)
        print("Home Full Name:    " + self.home_full_name)
        print("Away Location:     " + self.away_location)
        print("Away Team:         " + self.away_team)
        print("Away Abbreviation: " + self.away_abbreviation)
        print("Away Full Name:    " + self.away_full_name)
        print("Date/Time:         " + self.date)
        print("Venue:             " + self.venue)
        print("Is Home:           " + str(self.is_home))
        print("Team Hashtag:      " + self.team_hashtag)
        print("Game Hashtag:      " + self.game_hashtag)
        print("\n")


    def get_score_string(self, data):
        home_goals = get_home_goals(data)
        away_goals = get_away_goals(data)
        home_string = self.home_location + ": " + str(home_goals)
        away_string = self.away_location + ": " + str(away_goals)
        score_string = home_string + "\n" + away_string
        return score_string


    def get_shots_string(self):
        home_shots = get_home_shots(self.line_score)
        away_shots = get_away_shots(self.line_score)
        home_string = self.home_location + ": " + str(home_shots)
        away_string = self.away_location + ": " + str(away_shots)
        shots_string = "Shots On Goal\n" + home_string + "\n" + away_string
        return shots_string

    
    def get_period_string(self, data):
        period = data["about"]["period"]
        if period == 1:
            period_string = "The first period"
        elif period == 2:
            period_string = "The second period"
        elif period == 3:
            period_string = "The third period"
        else:
            period_string = "Period " + str(period)

        return period_string


    def get_team_string(self, data):
        team = data["team"]["name"]
        if team == self.home_full_name:
            team_string = self.home_location
        elif team == self.away_full_name:
            team_string = self.away_location
        else:
            raise("error - unknown team")
        return team_string


    #################################################################
    #  Event Strings
    #################################################################

    def get_game_scheduled_string(self, data):
        return ""

    
    def get_game_end_string(self, data):

        home_goals = get_home_goals(data)
        away_goals = get_away_goals(data)

        if home_goals > away_goals: 
            winner_string = self.home_location
        elif away_goals > home_goals:
            winner_string = self.away_location
        else:
            raise("error - no winnner")

        score_string = self.get_score_string(data)
        return "The game is over. " + winner_string + " wins." "\n\nFinal Score \n" + score_string


    def get_game_official_string(self, data):
        return ""


    def get_faceoff_string(self, data):
        return ""


    def get_stoppage_string(self, data):
        return ""


    def get_shot_string(self, data):
        # TODO: These are too spammy for primetime. These should be converted to a null event
        #       eventually. For now they're helpful for testing.
        # team_string = self.get_team_string(data)
        # shots_string = self.get_shots_string()
        # return "Shot on goal by " + team_string + ". \n\n" + get_description(data) + "\n\n" + shots_string
        return ""


    def get_hit_string(self, data):
        return ""


    def get_blocked_shot_string(self, data):
        return ""


    def get_giveaway_string(self, data):
        return ""


    def get_takeaway_string(self, data):
        return ""


    def get_missed_shot_string(self, data):
        return ""


    def get_penalty_string(self, data):
        team_string = self.get_team_string(data)
        penalty_name = data["result"]["secondaryType"]
        player_name = data["players"][0]["player"]["fullName"]
        penalty_minutes = data["result"]["penaltyMinutes"]
        penalty_severity = data["result"]["penaltySeverity"]
        return "There is a penalty on " + team_string + ".\n\n" + player_name + "\n" + str(penalty_minutes) + " minute " + penalty_severity.lower() + " for " + penalty_name.lower() + "."


    def get_period_ready_string(self, data):
        return ""


    def get_period_start_string(self, data):
        period_string = self.get_period_string(data)
        return period_string + " is starting at " + self.venue + "."


    def get_period_end_string(self, data):
        period_string = self.get_period_string(data)
        score_string = self.get_score_string(data)
        shots_string = self.get_shots_string()
        return period_string + " is over at " + self.venue + "." + "\n\nGoals\n" + score_string + "\n\n" + shots_string


    def get_period_official_string(self, data):
        return ""


    def get_goal_string(self, data):

        # TODO: The goal description isn't necessarily complete when sit first appears.
        #       We may need to post the goal scorer only first and then update (reply to the tweet)
        #       with the assists.

        team_string = self.get_team_string(data)
        player_name = get_player_name(data)
        score_string = self.get_score_string(data)
        goal_string = team_string + " goal! Scored by " + player_name + ".\n\n" + score_string
        return goal_string


    def get_official_challenge_string(self, data):
        team_string = self.get_team_string(data)
        challenge_string = team_string + " is challenging the ruling on the play."
        return challenge_string


    def get_event_string(self, data):

        event_type = data["result"]["event"]

        if event_type == blocked_shot_event:
            event_string = self.get_blocked_shot_string(data)
        elif event_type == challenge_event:
            event_string = self.get_official_challenge_string(data)
        elif event_type == faceoff_event:
            event_string = self.get_faceoff_string(data)
        elif event_type == game_end_event:
            event_string = self.get_game_end_string(data)
        elif event_type == game_official_event:
            event_string = self.get_game_official_string(data)
        elif event_type == game_scheduled_event:
            event_string = self.get_game_scheduled_string(data)
        elif event_type == giveaway_event: 
            event_string = self.get_giveaway_string(data)
        elif event_type == goal_event:       
            event_string = self.get_goal_string(data)
        elif event_type == hit_event:           
            event_string = self.get_hit_string(data)
        elif event_type == missed_shot_event:
            event_string = self.get_missed_shot_string(data)
        elif event_type == penalty_event:    
            event_string = self.get_penalty_string(data)
        elif event_type == period_end_event:
            event_string = self.get_period_end_string(data)
        elif event_type == period_official_event:
            event_string = self.get_period_official_string(data)
        elif event_type == period_ready_event:
            event_string = self.get_period_ready_string(data)
        elif event_type == period_start_event:
            event_string = self.get_period_start_string(data)
        elif event_type == shot_event:   
            event_string = self.get_shot_string(data)
        elif event_type == stoppage_event:
            event_string = self.get_stoppage_string(data)
        elif event_type == takeaway_event:
            event_string = self.get_takeaway_string(data)
        else:
            # TODO: Are there any missing events? These should be handled.
            # TODO: I'm guessing there might be special events for shootouts/OT
            raise("error - unhandled event")
        
        return event_string


    def print_event(self, data):
        event_string = self.get_event_string(data)
        if event_string != "":
            text = event_string #+ "\n\n" + self.game_hashtag + "\n"

            # Send the tweet
            if len(text) <= 240:
                print(text)
                self.tweeter.tweet(text)
            else:
                raise("error - the tweet is too long!")
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

class Printer:

    


    def __init__(self, data):
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


    def get_score_string(self, data):
        home_goals = data["about"]["goals"]["home"]
        away_goals = data["about"]["goals"]["away"]
        home_string = self.home_location + ": " + str(home_goals)
        away_string = self.away_location + ": " + str(away_goals)
        score_string = home_string + "\n" + away_string
        return score_string

    
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


    #################################################################
    #  Event Strings
    #################################################################

    def get_game_scheduled_string(self, data):
        return ""

    
    def get_game_end_string(self, data):

        home_goals = data["about"]["goals"]["home"]
        away_goals = data["about"]["goals"]["away"]

        if home_goals > away_goals: 
            winner_string = self.home_location
        elif away_goals > home_goals:
            winner_string = self.away_location
        else:
            winner_string = "Nobody"

        score_string = self.get_score_string(data)
        return "The game is over. " + winner_string + " wins." "\n\nFinal Score \n" + score_string


    def get_game_official_string(self, data):
        return ""


    def get_faceoff_string(self, data):
        return ""


    def get_stoppage_string(self, data):
        return ""


    def get_shot_string(self, data):
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
        return ""


    def get_period_ready_string(self, data):
        return ""


    def get_period_start_string(self, data):
        period_string = self.get_period_string(data)
        return period_string + " is starting at " + self.venue + "."


    def get_period_end_string(self, data):
        period_string = self.get_period_string(data)
        score_string = self.get_score_string(data)
        return period_string + " is over at " + self.venue + "." + "\n\n" + score_string


    def get_period_official_string(self, data):
        return ""


    def get_goal_string(self, data):
        score_string = self.get_score_string(data)
        goal_string = "GOAL! " + data["result"]["description"] + "\n\n" + score_string
        return goal_string


    def get_official_challenge_string(self, data):
        return ""


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
            print("unhandled event")
        
        return event_string


    def print_event(self, data):
        timestamp = data["about"]["dateTime"]
        event_string = self.get_event_string(data)
        if event_string != "":
            tweet_text = event_string + "\n\n" + self.game_hashtag + " " + self.team_hashtag

            # TODO: Send the tweet
            if len(tweet_text) <= 240:
                print(tweet_text)
            else:
                print("ERROR - the tweet is too long!")
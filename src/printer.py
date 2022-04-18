from src import logger
from src import tweeter
from src import templates

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


def get_player_name(data, player_type):

    for player in data["players"]:
        if player["playerType"].lower() == player_type.lower():
            return player["player"]["fullName"]

    logger.log_error("error - could not find player of type: " + player_type)
    return ""


def get_goal_scorer(data):
    return get_player_name(data, "Scorer")


def get_penalty_taker(data):
    return get_player_name(data, "penaltyOn")


class Printer:

    def get_game_data(self, data):
        self.home_location     = data["teams"]["home"]["locationName"]
        self.home_team         = data["teams"]["home"]["teamName"]
        self.home_abbreviation = data["teams"]["home"]["abbreviation"]
        self.home_full_name    = data["teams"]["home"]["name"]
        self.away_location     = data["teams"]["away"]["locationName"]
        self.away_team         = data["teams"]["away"]["teamName"]
        self.away_abbreviation = data["teams"]["away"]["abbreviation"]
        self.away_full_name    = data["teams"]["away"]["name"]
        self.date              = data["datetime"]["dateTime"]
        self.venue             = data["teams"]["home"]["venue"]["name"]
        self.is_home           = self.home_location == "Colorado"
        self.team_hashtag      = "#GoAvsGo"
        self.game_hashtag      = "#" + self.away_abbreviation + "vs" + self.home_abbreviation


    def update_line_score(self, line_score):
        self.line_score = line_score

        # TODO: Handle line score events, like the goalie being pulled


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


    def get_period_string(self, data):
        period = data["about"]["period"]
        if period == 1:
            period_string = "The first period"
        elif period == 2:
            period_string = "The second period"
        elif period == 3:
            period_string = "The third period"
        else:
            period_string = "The OT period"

        return period_string


    def get_team_string(self, data):
        team = data["team"]["name"]
        if team == self.home_full_name:
            team_string = self.home_location
        elif team == self.away_full_name:
            team_string = self.away_location
        else:
            logger.log_error("error - unknown team")
        return team_string


    #################################################################
    #  Event Strings
    #################################################################

    def get_game_scheduled_string(self, data):
        return ""

    
    def get_game_end_string(self, data):
        vars = { 
            "winner":     self.home_location if get_home_goals(data) > get_away_goals(data) else self.away_location,
            "home_team":  self.home_location, 
            "away_team":  self.away_location,
            "home_goals": get_home_goals(data),
            "away_goals": get_away_goals(data),
            "hashtags":   self.game_hashtag + " " + self.team_hashtag
        }
        return templates.game_end_template.format(**vars)


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

        # TODO: Should mention if there are any existing penalties
        #       and what the strength is post-penalty.

        severity = data["result"]["penaltySeverity"].lower()
        penalty_taker =  get_penalty_taker(data)

        # Don't tweet until the penalty taker is present
        if penalty_taker == "":
            return ""

        if severity == "penalty shot":

            vars = { 
                "team":     self.home_location if self.get_team_string(data) == self.away_location else self.away_location,
                "penalty":  data["result"]["secondaryType"].lower(),
                "player":   penalty_taker,
                "hashtags": self.game_hashtag + " " + self.team_hashtag
            }
            return templates.penalty_shot_template.format(**vars)

        else:

            vars = { 
                "team":     self.get_team_string(data),
                "penalty":  data["result"]["secondaryType"].lower(),
                "player":   penalty_taker,
                "minutes":  data["result"]["penaltyMinutes"],
                "severity": severity,
                "hashtags": self.game_hashtag + " " + self.team_hashtag
            }
            return templates.penalty_template.format(**vars)


    def get_period_ready_string(self, data):
        return ""


    def get_period_start_string(self, data):
        vars = { 
            "period":   self.get_period_string(data),
            "venue":    self.venue,
            "city":     self.home_location,
            "hashtags": self.game_hashtag + " " + self.team_hashtag
        }
        return templates.period_start_template.format(**vars)


    def get_period_end_string(self, data):
        vars = { 
            "period":     self.get_period_string(data),
            "venue":      self.venue,
            "home_team":  self.home_location, 
            "away_team":  self.away_location,
            "home_goals": get_home_goals(data),
            "away_goals": get_away_goals(data),
            "home_shots": get_home_shots(self.line_score),
            "away_shots": get_away_shots(self.line_score),
            "hashtags":   self.game_hashtag + " " + self.team_hashtag
        }
        return templates.period_end_template.format(**vars)


    def get_period_official_string(self, data):
        return ""


    def get_goal_string(self, data):

        # TODO: Should mention if this is a powerplay or shorthanded goal.

        scorer = get_goal_scorer(data)

        # Don't tweet until the scorer is present
        if scorer == "":
            return ""

        vars = { 
            "team":       self.get_team_string(data),
            "player":     scorer,
            "time":       data["about"]["periodTimeRemaining"],
            "period":     data["about"]["ordinalNum"],
            "home_team":  self.home_location, 
            "away_team":  self.away_location,
            "home_goals": get_home_goals(data),
            "away_goals": get_away_goals(data),
            "hashtags":   self.game_hashtag + " " + self.team_hashtag
        }
        return templates.goal_template.format(**vars)


    def get_official_challenge_string(self, data):

        # TODO: We should really include why they're challenging the play.
        #       The problem is that this information seems to be in the
        #       stoppage event that occurs prior to this one. Getting
        #       data from multiple events is going to be difficult with
        #       the current setup.

        vars = { 
            "team":     self.get_team_string(data),
            "hashtags": self.game_hashtag + " " + self.team_hashtag
        }
        return templates.challenge_template.format(**vars)


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
            logger.log_error("error - unhandled event: " + event_type)
        
        return event_string

    #################################################################
    #  Reply Strings
    #################################################################

    def get_game_scheduled_reply(self, previous_data, current_data):
        return ""

    
    def get_game_end_reply(self, previous_data, current_data):
        return ""

    def get_game_official_reply(self, previous_data, current_data):
        return ""


    def get_faceoff_reply(self, previous_data, current_data):
        return ""


    def get_stoppage_reply(self, previous_data, current_data):
        return ""


    def get_shot_reply(self, previous_data, current_data):
        return ""

    def get_hit_reply(self, previous_data, current_data):
        return ""


    def get_blocked_shot_reply(self, previous_data, current_data):
        return ""


    def get_giveaway_reply(self, previous_data, current_data):
        return ""


    def get_takeaway_reply(self, previous_data, current_data):
        return ""


    def get_missed_shot_reply(self, previous_data, current_data):
        return ""


    def get_penalty_reply(self, previous_data, current_data):
        return ""


    def get_period_ready_reply(self, previous_data, current_data):
        return ""


    def get_period_start_reply(self, previous_data, current_data):
        return ""


    def get_period_end_reply(self, previous_data, current_data):
        return ""


    def get_period_official_reply(self, previous_data, current_data):
        return ""


    def get_goal_reply(self, previous_data, current_data):
        return ""

        # TODO: The goal events are updated too frequently to post every time.
        #       They sometimes seem to flip the player's goal/assist totals
        #       back and forth between zero and the actual number.
        # 
        #       What we really want here is to post when the assists have been
        #       finalized. If there's an update later that changes the goal 
        #       scorer or the players with assists, we would want to tweet 
        #       that too. However, we can't just count on a delta between
        #       the JSON events indicating that something meaningful has
        #       changed.


    def get_official_challenge_reply(self, previous_data, current_data):
        return ""


    def get_reply_string(self, previous_data, current_data):

        event_type = current_data["result"]["event"]

        if event_type == blocked_shot_event:
            reply = self.get_blocked_shot_reply(previous_data, current_data)
        elif event_type == challenge_event:
            reply = self.get_official_challenge_reply(previous_data, current_data)
        elif event_type == faceoff_event:
            reply = self.get_faceoff_reply(previous_data, current_data)
        elif event_type == game_end_event:
            reply = self.get_game_end_reply(previous_data, current_data)
        elif event_type == game_official_event:
            reply = self.get_game_official_reply(previous_data, current_data)
        elif event_type == game_scheduled_event:
            reply = self.get_game_scheduled_reply(previous_data, current_data)
        elif event_type == giveaway_event: 
            reply = self.get_giveaway_reply(previous_data, current_data)
        elif event_type == goal_event:       
            reply = self.get_goal_reply(previous_data, current_data)
        elif event_type == hit_event:           
            reply = self.get_hit_reply(previous_data, current_data)
        elif event_type == missed_shot_event:
            reply = self.get_missed_shot_reply(previous_data, current_data)
        elif event_type == penalty_event:    
            reply = self.get_penalty_reply(previous_data, current_data)
        elif event_type == period_end_event:
            reply = self.get_period_end_reply(previous_data, current_data)
        elif event_type == period_official_event:
            reply = self.get_period_official_reply(previous_data, current_data)
        elif event_type == period_ready_event:
            reply = self.get_period_ready_reply(previous_data, current_data)
        elif event_type == period_start_event:
            reply = self.get_period_start_reply(previous_data, current_data)
        elif event_type == shot_event:   
            reply = self.get_shot_reply(previous_data, current_data)
        elif event_type == stoppage_event:
            reply = self.get_stoppage_reply(previous_data, current_data)
        elif event_type == takeaway_event:
            reply = self.get_takeaway_reply(previous_data, current_data)
        else:
            # TODO: Are there any missing events? These should be handled.
            # TODO: I'm guessing there might be special events for shootouts/OT
            logger.log_error("error - unhandled event for reply: " + event_type)
        
        return reply


    #################################################################
    #  Generators
    #################################################################

    def to_event_record(self, data):
        event_record = {
            "tweet_id": 0,
            "delay": False,
            "event": data
        }
        return event_record


    # TODO: This class being responsible for sending the tweets seems
    #       unnecessary. I think this class could probably just return
    #       the text of the tweets and replies and the tweeting could
    #       be done somewhere else. This dependency feels strange.

    def generate_tweet(self, data):
        tweet_id = 0
        text = self.get_event_string(data)
        if len(text) > 0:
            tweet_id = self.tweeter.tweet(text)
        return tweet_id

    
    def generate_reply(self, previous_data, current_data, id):
        tweet_id = 0
        text = self.get_reply_string(previous_data, current_data)
        if len(text) > 0:
            tweet_id = self.tweeter.reply(text, id)
        return tweet_id
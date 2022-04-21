"""
Description:
    This module is used to generate tweet text based on a given event.
"""

# Prevents the too many public functions warning. We should fix this.
# pylint: disable=R0904

from src import logger
from src import tweeter
from src import templates

BLOCKED_SHOT_EVENT    = "Blocked Shot"
CHALLENGE_EVENT       = "Official Challenge"
FACEOFF_EVENT         = "Faceoff"
GAME_END_EVENT        = "Game End"
GAME_OFFICIAL_EVENT   = "Game Official"
GAME_SCHEDULED_EVENT  = "Game Scheduled"
GIVEAWAY_EVENT        = "Giveaway"
GOAL_EVENT            = "Goal"
HIT_EVENT             = "Hit"
MISSED_SHOT_EVENT     = "Missed Shot"
PENALTY_EVENT         = "Penalty"
PERIOD_END_EVENT      = "Period End"
PERIOD_OFFICIAL_EVENT = "Period Official"
PERIOD_READY_EVENT    = "Period Ready"
PERIOD_START_EVENT    = "Period Start"
SHOT_EVENT            = "Shot"
STOPPAGE_EVENT        = "Stoppage"
TAKEAWAY_EVENT        = "Takeaway"


class UnknownTeam(Exception):
    """
    Description:
        An exception indicating that no team was found in an event.
    """

class UnknownPlayer(Exception):
    """
    Description:
        An exception indicating that no player was found in an event.
    """


def get_timestamp(event):
    """
    Description:
        Return the timestamp of the given event.
    """
    return event["about"]["dateTime"]


def get_description(event):
    """
    Description:
        Return the description from the given event.
    """
    return event["result"]["description"]


def get_home_goals(event):
    """
    Description:
        Return the number of goals by the home team in the given event.
    """
    return event["about"]["goals"]["home"]


def get_away_goals(event):
    """
    Description:
        Return the number of goals by the away team in the given event.
    """
    return event["about"]["goals"]["away"]


def get_home_shots(event):
    """
    Description:
        Return the number of shots by the home team in the given event.
    """
    return event["teams"]["home"]["shotsOnGoal"]


def get_away_shots(event):
    """
    Description:
        Return the number of shots by the away team in the given event.
    """
    return event["teams"]["away"]["shotsOnGoal"]


def get_period(event):
    """
    Description:
        Return the period from the given event.
    """
    return event["about"]["goals"]["away"]


def get_player_name(event, player_type):
    """
    Description:
        Return the name of the player with the given type from the event.
    """

    for player in event["players"]:
        if player["playerType"].lower() == player_type.lower():
            return player["player"]["fullName"]

    raise UnknownPlayer("Could not find player of type: " + player_type)


def get_goal_scorer(event):
    """
    Description:
        Return the goal scorer's name from the given event.
    """
    return get_player_name(event, "Scorer")


def get_penalty_taker(event):
    """
    Description:
        Return the penalty taker's name from the given event.
    """
    return get_player_name(event, "penaltyOn")


def get_period_string(event):
    """
    Description:
        Return a string represenation of the period from the given event.
    """
    period = event["about"]["period"]
    if period == 1:
        period_string = "The first period"
    elif period == 2:
        period_string = "The second period"
    elif period == 3:
        period_string = "The third period"
    else:
        period_string = "The OT period"
    return period_string


class Printer:
    """
    Description:
        This class is responsible for generating tweets.
    """

    def get_game_data(self, data):
        """
        Description:
            Set the class constants for the given game using the given
            game data.
        """
        self.game_data = {
            "home_location":     data["teams"]["home"]["locationName"],
            "home_team":         data["teams"]["home"]["teamName"],
            "home_abbreviation": data["teams"]["home"]["abbreviation"],
            "home_full_name":    data["teams"]["home"]["name"],
            "away_location":     data["teams"]["away"]["locationName"],
            "away_team":         data["teams"]["away"]["teamName"],
            "away_abbreviation": data["teams"]["away"]["abbreviation"],
            "away_full_name":    data["teams"]["away"]["name"],
            "date":              data["datetime"]["dateTime"],
            "venue":             data["teams"]["home"]["venue"]["name"]
        }


    def update_line_score(self, line_score):
        """
        Description:
            Update the line score record with the latest game data.
        """
        self.line_score = line_score


    def __init__(self, data):
        self.tweeter = tweeter.Tweeter()
        self.line_score = data["liveData"]["linescore"]
        self.get_game_data(data["gameData"])
        self.print_constants()


    #################################################################
    #  Helper Functions
    #################################################################

    def print_constants(self):
        """
        Description:
            Log the class constants for the current game.
        """
        logger.log_info("Home Location:     " + self.game_data.get("home_location", ""))
        logger.log_info("Home Team:         " + self.game_data.get("home_team", ""))
        logger.log_info("Home Abbreviation: " + self.game_data.get("home_abbreviation", ""))
        logger.log_info("Home Full Name:    " + self.game_data.get("home_full_name", ""))
        logger.log_info("Away Location:     " + self.game_data.get("away_location", ""))
        logger.log_info("Away Team:         " + self.game_data.get("away_team", ""))
        logger.log_info("Away Abbreviation: " + self.game_data.get("away_abbreviation", ""))
        logger.log_info("Away Full Name:    " + self.game_data.get("away_full_name", ""))
        logger.log_info("Date/Time:         " + self.game_data.get("date", ""))
        logger.log_info("Venue:             " + self.game_data.get("venue", ""))
        logger.log_info("Hashtags:          " + self.get_hashtags())


    def get_team_string(self, event):
        """
        Description:
            Return the name of the team from this event as a location name.
        """
        team = event["team"]["name"]
        if team == self.game_data.get("home_full_name"):
            team_string = self.get_home_location()
        elif team == self.game_data.get("away_full_name"):
            team_string = self.get_away_location()
        else:
            raise UnknownTeam()
        return team_string


    def get_home_location(self):
        """
        Description:
            Return the home team location from the game data.
        """
        return self.game_data.get("home_location", "")


    def get_away_location(self):
        """
        Description:
            Return the away team location from the game data.
        """
        return self.game_data.get("away_location", "")


    def get_home_abbreviation(self):
        """
        Description:
            Return the home team abbreviation from the game data.
        """
        return self.game_data.get("home_abbreviation", "")


    def get_away_abbreviation(self):
        """
        Description:
            Return the away team abbreviation from the game data.
        """
        return self.game_data.get("away_abbreviation", "")


    def get_opposition(self, team):
        """
        Description:
            Return the opposing team's location name.
        """
        home = self.get_home_location()
        away = self.get_away_location()
        return home if team == away else away


    def get_goal_leader(self, event):
        """
        Description:
            Return the team that is leading in goals scored.
        """
        home = self.get_home_location()
        away = self.get_away_location()
        return home if get_home_goals(event) > get_away_goals(event) else away


    def get_hashtags(self):
        """
        Description:
            Return the hashtags to append to all tweets.
        """
        home = self.get_home_abbreviation()
        away = self.get_away_abbreviation()
        game_hashtag = "#" + away + "vs" + home
        team_hashtag = "#GoAvsGo"
        return game_hashtag + " " + team_hashtag


    #################################################################
    #  Event Strings
    #################################################################``

    @staticmethod
    def get_null_event_string():
        """
        Description:
            Return the null event string for unhandled events.
        """
        return ""

    def get_game_scheduled_string(self, _event):
        """
        Description:
            Return the event string for a game scheduled event.
        """
        return self.get_null_event_string()


    def get_game_end_string(self, event):
        """
        Description:
            Return the event string for a game end event.
        """
        event_values = {
            "winner":     self.get_goal_leader(event),
            "home_team":  self.get_home_location(),
            "away_team":  self.get_away_location(),
            "home_goals": get_home_goals(event),
            "away_goals": get_away_goals(event),
            "hashtags":   self.get_hashtags()
        }
        return templates.GAME_END_TEMPLATE.format(**event_values)


    def get_game_official_string(self, _event):
        """
        Description:
            Return the event string for a game official event.
        """
        return self.get_null_event_string()


    def get_faceoff_string(self, _event):
        """
        Description:
            Return the event string for a faceoff event.
        """
        return self.get_null_event_string()


    def get_stoppage_string(self, _event):
        """
        Description:
            Return the event string for a stoppage event.
        """
        return self.get_null_event_string()


    def get_shot_string(self, _event):
        """
        Description:
            Return the event string for a shot event.
        """
        return self.get_null_event_string()


    def get_hit_string(self, _event):
        """
        Description:
            Return the event string for a hit event.
        """
        return self.get_null_event_string()


    def get_blocked_shot_string(self, _event):
        """
        Description:
            Return the event string for a blocked shot event.
        """
        return self.get_null_event_string()


    def get_giveaway_string(self, _event):
        """
        Description:
            Return the event string for a giveaway event.
        """
        return self.get_null_event_string()


    def get_takeaway_string(self, _event):
        """
        Description:
            Return the event string for a takeaway event.
        """
        return self.get_null_event_string()


    def get_missed_shot_string(self, _event):
        """
        Description:
            Return the event string for a missed shot event.
        """
        return self.get_null_event_string()


    def get_penalty_string(self, event):
        """
        Description:
            Return the event string for a penalty or penalty shot event.
        """

        severity = event["result"]["penaltySeverity"].lower()
        try:
            penalty_taker =  get_penalty_taker(event)
        except UnknownPlayer:
            logger.log_error("Could not determine penalty taker. Delaying tweet.")
            return self.get_null_event_string()

        if severity == "penalty shot":

            try:
                team = self.get_team_string(event)

                event_values = {
                    "team":     self.get_opposition(team),
                    "penalty":  event["result"]["secondaryType"].lower().replace("ps - ", ""),
                    "player":   penalty_taker,
                    "hashtags": self.get_hashtags()
                }
                event_string = templates.PENALTY_SHOT_TEMPLATE.format(**event_values)

            except UnknownTeam:
                logger.log_error("Could not determine penalized team. Delaying tweet.")
                event_string = ""

        else:

            try:
                team = self.get_team_string(event)

                event_values = {
                    "team":     team,
                    "penalty":  event["result"]["secondaryType"].lower(),
                    "player":   penalty_taker,
                    "minutes":  event["result"]["penaltyMinutes"],
                    "severity": severity,
                    "hashtags": self.get_hashtags()
                }
                event_string = templates.PENALTY_TEMPLATE.format(**event_values)

            except UnknownTeam:
                logger.log_error("Could not determine penalized team. Delaying tweet.")
                event_string = ""

        return event_string


    def get_period_ready_string(self, _event):
        """
        Description:
            Return the event string for a period ready event.
        """
        return self.get_null_event_string()


    def get_period_start_string(self, event):
        """
        Description:
            Return the event string for a period start event.
        """
        event_values = {
            "period":   get_period_string(event),
            "venue":    self.game_data.get("venue"),
            "city":     self.get_home_location(),
            "hashtags": self.get_hashtags()
        }
        return templates.PERIOD_START_TEMPLATE.format(**event_values)


    def get_period_end_string(self, event):
        """
        Description:
            Return the event string for a period end event.
        """
        event_values = {
            "period":     get_period_string(event),
            "venue":      self.game_data.get("venue"),
            "home_team":  self.get_home_location(),
            "away_team":  self.get_away_location(),
            "home_goals": get_home_goals(event),
            "away_goals": get_away_goals(event),
            "home_shots": get_home_shots(self.line_score),
            "away_shots": get_away_shots(self.line_score),
            "hashtags":   self.get_hashtags()
        }
        return templates.PERIOD_END_TEMPLATE.format(**event_values)


    def get_period_official_string(self, _event):
        """
        Description:
            Return the event string for a period official event.
        """
        return self.get_null_event_string()


    def get_goal_string(self, event):
        """
        Description:
            Return the event string for a goal event.
        """
        try:
            scorer = get_goal_scorer(event)
        except UnknownPlayer:
            logger.log_error("Could not determine goal scorer. Delaying tweet.")
            return self.get_null_event_string()

        strength = event["result"]["strength"]["code"]
        empty_net = event["result"]["emptyNet"]

        event_values = {
            "team":       self.get_team_string(event),
            "player":     scorer,
            "time":       event["about"]["periodTimeRemaining"],
            "period":     event["about"]["ordinalNum"],
            "home_team":  self.get_home_location(),
            "away_team":  self.get_away_location(),
            "home_goals": get_home_goals(event),
            "away_goals": get_away_goals(event),
            "hashtags":   self.get_hashtags()
        }

        if empty_net:
            goal_string = templates.EMPTY_NET_GOAL_TEMPLATE.format(**event_values)
        elif strength == "PPG":
            goal_string = templates.POWER_PLAY_GOAL_TEMPLATE.format(**event_values)
        elif strength == "SHG":
            goal_string = templates.SHORT_HANDED_GOAL_TEMPLATE.format(**event_values)
        else:
            goal_string = templates.GOAL_TEMPLATE.format(**event_values)

        return goal_string


    def get_official_challenge_string(self, event):
        """
        Description:
            Return the event string for a challenge event.
        """
        event_values = {
            "team":     self.get_team_string(event),
            "hashtags": self.get_hashtags()
        }
        return templates.CHALLENGE_TEMPLATE.format(**event_values)


    def get_event_string(self, event):
        """
        Description:
            Return the event string for an event.
        """
        event_lookup = {
            BLOCKED_SHOT_EVENT:    self.get_blocked_shot_string,
            CHALLENGE_EVENT:       self.get_official_challenge_string,
            FACEOFF_EVENT:         self.get_faceoff_string,
            GAME_END_EVENT:        self.get_game_end_string,
            GAME_OFFICIAL_EVENT:   self.get_game_official_string,
            GAME_SCHEDULED_EVENT:  self.get_game_scheduled_string,
            GIVEAWAY_EVENT:        self.get_giveaway_string,
            GOAL_EVENT:            self.get_goal_string,
            HIT_EVENT:             self.get_hit_string,
            MISSED_SHOT_EVENT:     self.get_missed_shot_string,
            PENALTY_EVENT:         self.get_penalty_string,
            PERIOD_END_EVENT:      self.get_period_end_string,
            PERIOD_OFFICIAL_EVENT: self.get_period_official_string,
            PERIOD_READY_EVENT:    self.get_period_ready_string,
            PERIOD_START_EVENT:    self.get_period_start_string,
            SHOT_EVENT:            self.get_shot_string,
            STOPPAGE_EVENT:        self.get_stoppage_string,
            TAKEAWAY_EVENT:        self.get_takeaway_string
        }

        event_type = event["result"]["event"]
        try:
            event_string = event_lookup[event_type](event)
        except KeyError:
            logger.log_error("error - unhandled event: " + event_type)

        return event_string


    #################################################################
    #  Reply Strings
    #################################################################

    def get_game_scheduled_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a game scheduled event.
        """
        return self.get_null_event_string()


    def get_game_end_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a game end event.
        """
        return self.get_null_event_string()


    def get_game_official_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a game scheduled event.
        """
        return self.get_null_event_string()


    def get_faceoff_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a faceoff event.
        """
        return self.get_null_event_string()


    def get_stoppage_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a stoppage event.
        """
        return self.get_null_event_string()


    def get_shot_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a shot event.
        """
        return self.get_null_event_string()


    def get_hit_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a hit event.
        """
        return self.get_null_event_string()


    def get_blocked_shot_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a blocked shot event.
        """
        return self.get_null_event_string()


    def get_giveaway_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a giveaway event.
        """
        return self.get_null_event_string()


    def get_takeaway_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a takeaway event.
        """
        return self.get_null_event_string()


    def get_missed_shot_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a missed shot event.
        """
        return self.get_null_event_string()


    def get_penalty_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a penalty event.
        """
        return self.get_null_event_string()


    def get_period_ready_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a period ready event.
        """
        return self.get_null_event_string()


    def get_period_start_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a period start event.
        """
        return self.get_null_event_string()


    def get_period_end_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a period end event.
        """
        return self.get_null_event_string()


    def get_period_official_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a period official event.
        """
        return self.get_null_event_string()


    def get_goal_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a goal event.
        """
        return self.get_null_event_string()


    def get_official_challenge_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a challenge event.
        """
        return self.get_null_event_string()


    def get_reply_string(self, previous_event, current_event):
        """
        Description:
            Return the reply string for an event.
        """
        event_lookup = {
            BLOCKED_SHOT_EVENT:    self.get_blocked_shot_reply,
            CHALLENGE_EVENT:       self.get_official_challenge_reply,
            FACEOFF_EVENT:         self.get_faceoff_reply,
            GAME_END_EVENT:        self.get_game_end_reply,
            GAME_OFFICIAL_EVENT:   self.get_game_official_reply,
            GAME_SCHEDULED_EVENT:  self.get_game_scheduled_reply,
            GIVEAWAY_EVENT:        self.get_giveaway_reply,
            GOAL_EVENT:            self.get_goal_reply,
            HIT_EVENT:             self.get_hit_reply,
            MISSED_SHOT_EVENT:     self.get_missed_shot_reply,
            PENALTY_EVENT:         self.get_penalty_reply,
            PERIOD_END_EVENT:      self.get_period_end_reply,
            PERIOD_OFFICIAL_EVENT: self.get_period_official_reply,
            PERIOD_READY_EVENT:    self.get_period_ready_reply,
            PERIOD_START_EVENT:    self.get_period_start_reply,
            SHOT_EVENT:            self.get_shot_reply,
            STOPPAGE_EVENT:        self.get_stoppage_reply,
            TAKEAWAY_EVENT:        self.get_takeaway_reply
        }

        event_type = current_event["result"]["event"]
        try:
            reply = event_lookup[event_type](previous_event, current_event)
        except KeyError:
            logger.log_error("error - unhandled event: " + event_type)

        return reply

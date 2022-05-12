"""
Description:
    This module is used to generate tweet text based on a given event.
"""

# Prevents the too many public functions warning. We should fix this.
# pylint: disable=R0904

from src import events
from src import logger
from src import tweeter
from src import templates

TEAM_HASHTAG    = "#GoAvsGo"
PLAYOFF_HASHTAG = "#FindAWay"

def get_home_shots(data):
    """
    Description:
        Return the number of shots by the home team in the current line score.
    """
    return data["teams"]["home"]["shotsOnGoal"]


def get_away_shots(data):
    """
    Description:
        Return the number of shots by the away team in the current line score.
    """
    return data["teams"]["away"]["shotsOnGoal"]


def get_period_string(event):
    """
    Description:
        Return a string represenation of the period from the given event.
    """
    if event.period == 1:
        period_string = "The first period"
    elif event.period == 2:
        period_string = "The second period"
    elif event.period == 3:
        period_string = "The third period"
    else:
        period_string = "The OT period"
    return period_string

def get_ordinal_period_string(event):
    """
    Description:
        Return an ordinal string represenation of the period from the given event.
    """
    if event.period == 1:
        period_string = "1st"
    elif event.period == 2:
        period_string = "2nd"
    elif event.period == 3:
        period_string = "3rd"
    elif event.period == 4:
        period_string = "OT"
    elif event.period == 5:
        period_string = "2OT"
    elif event.period == 6:
        period_string = "3OT"
    elif event.period == 7:
        period_string = "4OT"
    else:
        period_string = "OT"
    return period_string


class Generator:
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
            "venue":             data["teams"]["home"]["venue"]["name"],
            "is_playoffs":       data["game"]["type"] == "P"
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
        logger.log_info("Is Playoffs:       " + str(self.game_data.get("is_playoffs", False)))
        logger.log_info("Hashtags:          " + self.get_hashtags())


    def get_team_string(self, team):
        """
        Description:
            Return the name of the team from this event as a location name.
        """
        if team == self.game_data.get("home_full_name"):
            team_string = self.get_home_location()
        elif team == self.game_data.get("away_full_name"):
            team_string = self.get_away_location()
        else:
            logger.log_error("unknown team: " + team)
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
        if team == self.game_data.get("home_full_name"):
            team_string = self.get_away_location()
        elif team == self.game_data.get("away_full_name"):
            team_string = self.get_home_location()
        else:
            logger.log_error("unknown team: " + team)
        return team_string


    def get_goal_leader(self, event):
        """
        Description:
            Return the team that is leading in goals scored.
        """
        home = self.get_home_location()
        away = self.get_away_location()
        return home if event.home_goals > event.away_goals else away


    def get_hashtags(self):
        """
        Description:
            Return the hashtags to append to all tweets.
        """
        hashtags = []
        hashtags.append("#" + self.get_away_abbreviation() + "vs" + self.get_home_abbreviation())
        hashtags.append(TEAM_HASHTAG)
        if self.game_data["is_playoffs"]:
            hashtags.append(PLAYOFF_HASHTAG)
        return " ".join(hashtags)


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
            "home_goals": event.home_goals,
            "away_goals": event.away_goals,
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

        if event.taker is None:
            logger.log_error("Could not determine penalty taker. Delaying tweet.")
            return self.get_null_event_string()

        if event.reason is None:
            logger.log_error("Could not determine penalty. Delaying tweet.")
            return self.get_null_event_string()

        if event.team is None:
            logger.log_error("Could not determine penalized team. Delaying tweet.")
            return self.get_null_event_string()

        event_values = {
            "team":     self.get_team_string(event.team),
            "penalty":  event.reason,
            "player":   event.taker,
            "minutes":  event.minutes,
            "severity": event.severity,
            "hashtags": self.get_hashtags()
        }
        event_string = templates.PENALTY_TEMPLATE.format(**event_values)

        return event_string


    def get_penalty_shot_string(self, event):
        """
        Description:
            Return the event string for a penalty or penalty shot event.
        """

        if event.taker is None:
            logger.log_error("Could not determine penalty taker. Delaying tweet.")
            return self.get_null_event_string()

        if event.reason is None:
            logger.log_error("Could not determine penalty. Delaying tweet.")
            return self.get_null_event_string()

        if event.team is None:
            logger.log_error("Could not determine penalized team. Delaying tweet.")
            return self.get_null_event_string()

        event_values = {
            "team":     self.get_opposition(event.team),
            "penalty":  event.reason,
            "player":   event.taker,
            "hashtags": self.get_hashtags()
        }
        event_string = templates.PENALTY_SHOT_TEMPLATE.format(**event_values)

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
            "home_goals": event.home_goals,
            "away_goals": event.away_goals,
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
        if event.scorer is None:
            logger.log_error("Could not determine goal scorer. Delaying tweet.")
            return self.get_null_event_string()

        event_values = {
            "team":             self.get_team_string(event.team),
            "scorer":           event.scorer,
            "primary_assist":   event.primary_assist,
            "secondary_assist": event.secondary_assist,
            "description":      event.description,
            "time":             event.time,
            "period":           get_ordinal_period_string(event),
            "home_team":        self.get_home_location(),
            "away_team":        self.get_away_location(),
            "home_goals":       event.home_goals,
            "away_goals":       event.away_goals,
            "hashtags":         self.get_hashtags()
        }

        if event.is_empty_net:
            goal_string = templates.EMPTY_NET_GOAL_TEMPLATE.format(**event_values)
        elif event.strength == "PPG":
            goal_string = templates.POWER_PLAY_GOAL_TEMPLATE.format(**event_values)
        elif event.strength == "SHG":
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
            "team":     self.get_team_string(event.team),
            "hashtags": self.get_hashtags()
        }
        return templates.CHALLENGE_TEMPLATE.format(**event_values)


    def get_event_string(self, event):
        """
        Description:
            Return the event string for an event.
        """
        event_lookup = {
            events.BlockedShot:    self.get_blocked_shot_string,
            events.Challenge:      self.get_official_challenge_string,
            events.Faceoff:        self.get_faceoff_string,
            events.GameEnd:        self.get_game_end_string,
            events.GameOfficial:   self.get_game_official_string,
            events.GameScheduled:  self.get_game_scheduled_string,
            events.Giveaway:       self.get_giveaway_string,
            events.Goal:           self.get_goal_string,
            events.Hit:            self.get_hit_string,
            events.MissedShot:     self.get_missed_shot_string,
            events.Penalty:        self.get_penalty_string,
            events.PenaltyShot:    self.get_penalty_shot_string,
            events.PeriodEnd:      self.get_period_end_string,
            events.PeriodOfficial: self.get_period_official_string,
            events.PeriodReady:    self.get_period_ready_string,
            events.PeriodStart:    self.get_period_start_string,
            events.Shot:           self.get_shot_string,
            events.Stoppage:       self.get_stoppage_string,
            events.Takeaway:       self.get_takeaway_string
        }

        try:
            event_string = event_lookup[event.__class__](event)
        except KeyError:
            logger.log_error("error - unhandled event: " + str(event))

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


    def get_penalty_shot_reply(self, _previous_event, _current_event):
        """
        Description:
            Return the reply string for a penalty shot event.
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


    def get_goal_reply(self, previous_event, current_event):
        """
        Description:
            Return the reply string for a goal event.
        """

        event_values = {
            "team":             self.get_team_string(current_event.team),
            "scorer":           current_event.scorer,
            "primary_assist":   current_event.primary_assist,
            "secondary_assist": current_event.secondary_assist,
            "description":      current_event.description,
            "time":             current_event.time,
            "period":           get_ordinal_period_string(current_event),
            "home_team":        self.get_home_location(),
            "away_team":        self.get_away_location(),
            "home_goals":       current_event.home_goals,
            "away_goals":       current_event.away_goals,
            "hashtags":         self.get_hashtags()
        }

        update_count              = 0
        scorer_modified           = previous_event.scorer != current_event.scorer
        primary_assist_added      = (
            previous_event.primary_assist is None and
            current_event.primary_assist is not None
        )
        secondary_assist_added    = (
            previous_event.secondary_assist is None and
            current_event.secondary_assist is not None
        )
        primary_assist_modified   = (
            previous_event.primary_assist is not None and
            previous_event.primary_assist != current_event.primary_assist
        )
        secondary_assist_modified = (
            previous_event.secondary_assist is not None and
            previous_event.secondary_assist != current_event.secondary_assist
        )

        # Goal scorer has been changed
        if scorer_modified:
            update_count += 1
            update_text = templates.SCORER_UPDATE_TEMPLATE.format(**event_values)

        # Assists have been added
        if primary_assist_added and secondary_assist_added:
            update_count += 1
            update_text = templates.ASSIST_ADD_BOTH_TEMPLATE.format(**event_values)
        elif primary_assist_added:
            update_count += 1
            update_text = templates.ASSIST_ADD_PRIMARY_TEMPLATE.format(**event_values)
        elif secondary_assist_added:
            update_count += 1
            update_text = templates.ASSIST_ADD_SECONDARY_TEMPLATE.format(**event_values)

        # Assists have been changed
        if primary_assist_modified and secondary_assist_modified:
            update_count += 1
            update_text = templates.ASSIST_UPDATE_TEMPLATE.format(**event_values)
        elif primary_assist_modified:
            update_count += 1
            update_text = templates.PRIMARY_ASSIST_UPDATE_TEMPLATE.format(**event_values)
        elif secondary_assist_modified:
            update_count += 1
            update_text = templates.SECONDARY_ASSIST_UPDATE_TEMPLATE.format(**event_values)

        # Time of goal has been changed
        if previous_event.time != current_event.time:
            update_count += 1
            update_text = templates.GOAL_TIME_UPDATE_TEMPLATE.format(**event_values)

        # More than one update occurred, print a generic update
        if update_count > 1:
            update_text = templates.GOAL_REPLY_TEMPLATE.format(**event_values)

        return update_text


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
            events.BlockedShot:    self.get_blocked_shot_reply,
            events.Challenge:      self.get_official_challenge_reply,
            events.Faceoff:        self.get_faceoff_reply,
            events.GameEnd:        self.get_game_end_reply,
            events.GameOfficial:   self.get_game_official_reply,
            events.GameScheduled:  self.get_game_scheduled_reply,
            events.Giveaway:       self.get_giveaway_reply,
            events.Goal:           self.get_goal_reply,
            events.Hit:            self.get_hit_reply,
            events.MissedShot:     self.get_missed_shot_reply,
            events.Penalty:        self.get_penalty_reply,
            events.PenaltyShot:    self.get_penalty_shot_reply,
            events.PeriodEnd:      self.get_period_end_reply,
            events.PeriodOfficial: self.get_period_official_reply,
            events.PeriodReady:    self.get_period_ready_reply,
            events.PeriodStart:    self.get_period_start_reply,
            events.Shot:           self.get_shot_reply,
            events.Stoppage:       self.get_stoppage_reply,
            events.Takeaway:       self.get_takeaway_reply
        }
        try:
            reply = event_lookup[current_event.__class__](previous_event, current_event)
        except KeyError:
            logger.log_error("error - unhandled event: " + current_event.__class__)

        return reply

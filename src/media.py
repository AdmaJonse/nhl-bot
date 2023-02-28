"""
This package provides utilities for retrieving game media (such as video
highlights) from the NHL's webiste.
"""

from typing import Any, Optional

from datetime import datetime, timedelta
import requests

from src import feed
from src import logger
from src.output import templates
from src.output import output


NHL_API_URL : str = "https://statsapi.web.nhl.com/api/v1/game/"


def check_for_data(method):
    """
    Decorator that will ensure we have current data prior to running the
    function that follows.
    """
    def wrapper(self, *args):
        if (datetime.now() - self.data_time) > timedelta(seconds=5):
            self.get_data()
        return method(self, *args)
    return wrapper

def get_id(highlight : str) -> int:
    """
    Return the video corresponding to the given event ID.
    """
    return int(highlight["id"])


def get_event_id(highlight : str) -> Optional[int]:
    """
    Return the event ID associated with this highlight.
    """
    for keyword in highlight["keywords"]:
        if keyword["type"] == "statsEventId":
            return int(keyword["value"])
    return None


def get_description(highlight : str) -> str:
    """
    Return the description of this highlight.
    """
    return highlight["description"]


def get_url(highlight : str):
    """
    Return the video url for this highlight.
    """
    video_format : str = "FLASH_1800K_896x504"
    for video in highlight["playbacks"]:
        if video["name"] == video_format:
            return video["url"]
    logger.log_error("Could not find highlight matching expected format: " + video_format)
    return None


class Parser:
    """
    This class is used to parse game media for a particular game.
    """

    def __init__(self, feed_parser : feed.Parser):
        self.game_id   : int         = feed_parser.game_id
        self.data_time : datetime    = datetime.now()
        self.data      : Any         = []
        self.count     : int         = 0
        self.processed : list        = []
        self.feed      : feed.Parser = feed_parser


    def get_data(self):
        """
        This function retrieves the latest JSON data record for the current
        game from the NHL website.
        """
        url       : str = NHL_API_URL + str(self.game_id) + "/content"
        params    : str = ""
        request   : Any = requests.get(url, params)
        self.data       = request.json()
        self.data_time  = datetime.now()


    @check_for_data
    def get_highlights(self):
        """
        Return the full highlight JSON record for the given event ID.
        """
        if self.data == []:
            return None
        return self.data["highlights"]["gameCenter"]["items"]


    @check_for_data
    def get_highlight(self, event_id : int):
        """
        Return the full highlight JSON record for the given event ID.
        """
        for highlight in self.get_highlights():
            if get_event_id(highlight) == event_id:
                return highlight
        return None


    @check_for_data
    def get_post(self, highlight : str) -> str:
        """
        Create a post using the given highlight.
        """
        event_values = {
            "description": get_description(highlight),
            "hashtags":    "#GoAvsGo"
        }
        return templates.HIGHLIGHT_TEMPLATE.format(**event_values)


    @check_for_data
    def new_highlight_exists(self) -> bool:
        """
        Check if any new unprocessed highlights exist on the content page.
        """
        highlights = self.get_highlights()
        count = (0 if highlights is None else len(highlights))
        if count > self.count:
            self.count = count
            return True
        return False


    def process_highlight(self, highlight : str):
        """
        Create a post for the given highlight.
        """
        self.processed.append(get_id(highlight))
        event_id = get_event_id(highlight)
        if event_id is not None:
            event = self.feed.get_event(event_id)
            if event is not None:
                if event.has_tweeted:
                    parent = event.tweet_id
                    post = self.get_post(highlight)
                    url = get_url(highlight)
                    output.reply_with_media(parent, post, url)
                else:
                    logger.log_error("Could not post highlight because there is no parent tweet.")
        else:
            logger.log_error("Could not find an event ID when parsing the highlight.")


    @check_for_data
    def parse(self):
        """
        Parse the content page for the current game to determine if there are any new
        highlights to post.
        """
        if self.new_highlight_exists():
            for highlight in self.get_highlights():
                if get_id(highlight) not in self.processed:
                    self.process_highlight(highlight)

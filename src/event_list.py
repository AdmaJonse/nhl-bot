"""
This module defines a list of Events that have been processed.
"""

from typing import Dict, Optional

from src.events.event import Event
from src.logger import log

import src.generator


class EventList:
    """
    This class defines a list of Events that have been processed.
    """

    def __init__(self):
        self._events: Dict[str, Event] = {}


    def add(self, event: Event) -> None:
        """
        Add a new event to the list. If this event already exists in the list, update it and post
        a reply. If this is a new event, add the event and create a new post.
        """
        if self.exists(event.id):
            previous: Optional[Event] = self.get(event.id)
            if previous is not None:
                src.generator.generator.create_reply(event, previous)
        else:
            src.generator.generator.create_post(event)

        self._events[event.id] = event


    def exists(self, event_id: str) -> bool:
        """
        Check if an event with the given ID already exists in the list.
        """
        return event_id in self._events


    def get(self, event_id: str) -> Optional[Event]:
        """
        Return the Event with the given ID. If an event with this ID does not exist, return None.
        """
        if self.exists(event_id):
            return self._events[event_id]
        return None


    def get_from_api_id(self, event_id: int) -> Optional[Event]:
        """
        Return the event with the given NHL API event ID.
        """
        for item in self._events.values():
            if item.event_id == event_id:
                return item
        log.error("Could not find event with ID: " + str(event_id))
        return None


    def clear(self) -> None:
        """
        Clear the list of events.
        """
        self._events = {}


event_list: EventList = EventList()

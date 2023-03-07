"""
This module defines a list of all highlights that have been processed.
"""

from typing import Dict, Optional

from src.generator import generator
from src.data.highlight import Highlight
from src.event_list import event_list

class HighlightList:
    """
    This class defines a list of all highlights that have been processed.
    """

    def __init__(self):
        self.highlights : Dict[int, Highlight] = {}


    def add(self, highlight : Highlight) -> None:
        """
        Add a new highlight to the list. If it does not already exist, post the highlight.
        """
        if highlight.id not in self.highlights:
            self.highlights[highlight.id] = highlight
            event = event_list.get_from_api_id(highlight.event_id)
            if event is not None:
                generator.create_highlight(highlight, event)


    def exists(self, highlight_id : int) -> bool:
        """
        Return a boolean indicating whether or not this highlight ID exists in the list of
        processed highlights.
        """
        return highlight_id in self.highlights


    def get(self, highlight_id : int) -> Optional[Highlight]:
        """
        Return the highlight with the given ID from the list.
        """
        for highlight in self.highlights.values():
            if highlight.id == highlight_id:
                return highlight
        return None


    def clear(self) -> None:
        """
        Clear the list of highlights.
        """
        self.highlights = {}


highlight_list : HighlightList = HighlightList()

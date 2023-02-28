"""
This module stores exceptions that will be raised and handled by the application.
"""

class InsufficientData(Exception):
    """
    An exception that will be raised when the given data is missing a required field.
    """


class HighlightNotFound(Exception):
    """
    Exception raised when no highlight exists for this event.
    """

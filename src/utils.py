"""
Utility functions that may be used throughout the application.
"""

from typing import List, Optional

def initials(text : Optional[str]) -> str:
    """
    Generate the initials of the given string.
    """
    if text is None:
        return ""

    words  : List[str] = text.split()
    result : str       = ""

    for word in words:
        result += word[0].upper()

    return result


def pad(text : Optional[str], length : int) -> str:
    """
    Pad the given string with spaces so that it has the specified length.
    """

    if text is None:
        return '#'*length

    result : str = ""

    if len(text) > length:
        result = text[:length]
    else:
        result = text.ljust(length, '#')

    return result

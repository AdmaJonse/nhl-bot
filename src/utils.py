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


def pad(text : Optional[str], length : int, align : str = "left") -> str:
    """
    Pad the given string with spaces so that it has the specified length.
    """

    result : str = ""
    fill   : str = ' '

    if text is None:
        return fill*length

    text = text.replace(' ','')

    if len(text) > length:
        result = text[:length]
    else:
        if align == "left":
            result = text.ljust(length, fill)
        else:
            result = text.rjust(length, fill)

    return result.upper()


def pad_code(text : Optional[str]) -> str:
    """
    Pad the code string.
    """
    length : int = 10
    return pad(text, length, "right")


def pad_blob(text : Optional[str]) -> str:
    """
    Pad the blob string.
    """
    length : int = 6
    return pad(text, length, "left")

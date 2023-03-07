"""
This module defines the Parse command.
"""

from src.command.command import Command, Priority
from src.parsers import parsers


class Parse(Command):
    """
    This class defines the Parse command. It will be called periodically and trigger a parse
    from all registered parsers.
    """

    def __init__(self):
        super().__init__("Parse", Priority.NORMAL)


    def execute(self) -> None:
        """
        Trigger a parse from all registered parsers.
        """
        parsers.parse()

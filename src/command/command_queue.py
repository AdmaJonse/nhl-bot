"""
This module defines the command queue class.
"""

from enum import Enum
from queue import PriorityQueue

from src.command.command import Command, Priority
from src.logger import log

class State(Enum):
    """
    The state of the command queue.
    """
    STOPPED  = 1
    RUNNING  = 2
    STOPPING = 3

class ShutdownException(Exception):
    """
    Exception used to shutdown the command queue.
    """

class Shutdown(Command):
    """
    The command used to stop the command queue.
    """
    def __init__(self):
        super().__init__("Shutdown", Priority.NORMAL)

    def execute(self) -> None:
        raise ShutdownException()


class CommandQueue:
    """
    The Command Queue is responsible for executing the commands that are enqueued.
    """

    def __init__(self):
        self.queue : PriorityQueue = PriorityQueue()
        self.state : State         = State.STOPPED

    def enqueue(self, command : Command):
        """
        Enqueue the given Command in the command queue.
        """
        self.queue.put(command)

    def start(self):
        """
        Start processing commands from the queue.
        """
        self.state = State.RUNNING
        while True:
            if not self.queue.empty():
                try:
                    command : Command = self.queue.get()
                    command.execute()
                except ShutdownException:
                    log.info("Stopping the command server.")
                    self.state = State.STOPPED
                    break

    def stop(self):
        """
        Stop processing commands from the queue.
        """
        self.state = State.STOPPING
        self.enqueue(Shutdown())

command_queue = CommandQueue()

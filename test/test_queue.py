"""
Test the order of commands in the command queue.
"""


import unittest

from src.command.command import Command, Priority
from src.command.command_queue import CommandQueue

class A(Command):
    def __init__(self):
        super().__init__("A", Priority.NORMAL)
    def execute(self) -> None:
        pass

class B(Command):
    def __init__(self):
        super().__init__("B", Priority.NORMAL)
    def execute(self) -> None:
        pass

class C(Command):
    def __init__(self):
        super().__init__("C", Priority.NORMAL)
    def execute(self) -> None:
        pass

class D(Command):
    def __init__(self):
        super().__init__("D", Priority.NORMAL)
    def execute(self) -> None:
        pass

class E(Command):
    def __init__(self):
        super().__init__("E", Priority.NORMAL)
    def execute(self) -> None:
        pass

class F(Command):
    def __init__(self):
        super().__init__("F", Priority.HIGH)
    def execute(self) -> None:
        pass

class G(Command):
    def __init__(self):
        super().__init__("G", Priority.NORMAL)
    def execute(self) -> None:
        pass

class H(Command):
    def __init__(self):
        super().__init__("H", Priority.HIGH)
    def execute(self) -> None:
        pass

class TestQueue(unittest.TestCase):
    """
    Unit tests for the command queue.
    """

    def test_command_order(self):
        """
        Test the order of commands in the priority queue.
        """
        queue = CommandQueue()

        queue.enqueue(A())
        queue.enqueue(B())
        queue.enqueue(C())
        queue.enqueue(D())

        self.assertEqual(queue.dequeue().name, "A")
        self.assertEqual(queue.dequeue().name, "B")
        self.assertEqual(queue.dequeue().name, "C")
        self.assertEqual(queue.dequeue().name, "D")

        queue.enqueue(E())
        queue.enqueue(F())
        queue.enqueue(G())
        queue.enqueue(H())

        self.assertEqual(queue.dequeue().name, "F")
        self.assertEqual(queue.dequeue().name, "H")
        self.assertEqual(queue.dequeue().name, "E")
        self.assertEqual(queue.dequeue().name, "G")

        queue.enqueue(A())
        queue.enqueue(B())
        queue.enqueue(C())
        queue.enqueue(D())
        queue.enqueue(E())
        queue.enqueue(F())
        queue.enqueue(G())
        queue.enqueue(H())

        self.assertEqual(queue.dequeue().name, "F")
        self.assertEqual(queue.dequeue().name, "H")
        self.assertEqual(queue.dequeue().name, "A")
        self.assertEqual(queue.dequeue().name, "B")
        self.assertEqual(queue.dequeue().name, "C")
        self.assertEqual(queue.dequeue().name, "D")
        self.assertEqual(queue.dequeue().name, "E")
        self.assertEqual(queue.dequeue().name, "G")

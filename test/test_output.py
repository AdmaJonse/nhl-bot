import unittest

from src.output.output import output

class TestGenerator(unittest.TestCase):
    """
    Unit tests for the generator class.
    """

    def test_not_dry_run(self):
        """
        Prevent a push when dry run is enabled.
        """
        self.assertFalse(output.dry_run)

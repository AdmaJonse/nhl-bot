import unittest

from src import output

class TestGenerator(unittest.TestCase):
    """
    Description:
        Unit tests for the generator class.
    """

    def test_not_dry_run(self):
        """
        Description:
            Prevent a push when dry run is enabled.
        """
        self.assertFalse(output.is_dry_run())

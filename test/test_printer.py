import unittest

from src import printer
from test import test_data

class TestPrinter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.printer = printer.Printer(test_data.game_data)


    #################################################
    # Event Posts
    #################################################

    def test_game_scheduled(self):
        actual   = self.printer.get_game_scheduled_string(test_data.game_scheduled_data)
        expected = ""
        self.assertEqual(expected, actual)

    
    def test_game_end(self):
        actual   = self.printer.get_game_end_string(test_data.game_end_data)
        expected = "\nThe game is over. Washington wins!\n\nFinal Score:\nWashington: 4\nBoston: 2\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_game_official(self):
        actual   = self.printer.get_game_official_string(test_data.game_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff(self):
        actual   = self.printer.get_faceoff_string(test_data.faceoff_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage(self):
        actual   = self.printer.get_stoppage_string(test_data.stoppage_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot(self):
        actual   = self.printer.get_shot_string(test_data.shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit(self):
        actual   = self.printer.get_hit_string(test_data.hit_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot(self):
        actual   = self.printer.get_blocked_shot_string(test_data.blocked_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway(self):
        actual   = self.printer.get_giveaway_string(test_data.giveaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway(self):
        actual   = self.printer.get_takeaway_string(test_data.takeaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot(self):
        actual   = self.printer.get_missed_shot_string(test_data.missed_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty(self):
        actual   = self.printer.get_penalty_string(test_data.penalty_data)
        expected = "\nThere is a penalty on Washington.\n\nNic Dowd\n2 minute minor for hi-sticking\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_penalty_no_taker(self):
        actual   = self.printer.get_penalty_string(test_data.penalty_data_no_taker)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_shot(self):
        actual   = self.printer.get_penalty_string(test_data.penalty_shot_data)
        expected = "\nThat's a penalty shot for Washington!\n\nThe infraction is against Brenden Dillon for ps - hooking on breakaway.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_ready(self):
        actual   = self.printer.get_period_ready_string(test_data.period_ready_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start(self):
        actual   = self.printer.get_period_start_string(test_data.period_start_data)
        expected = "\nThe second period is starting at Capital One Arena in Washington.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_end(self):
        actual   = self.printer.get_period_end_string(test_data.period_end_data)
        expected = "\nThe first period is over at Capital One Arena.\n\nGoals\nWashington: 0\nBoston: 0\n\nShots on Goal\nWashington: 33\nBoston: 30\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_period_official(self):
        actual   = self.printer.get_period_official_string(test_data.period_official_data)
        expected = ""
        self.assertEqual(expected, actual)

    
    def test_goal(self):
        actual   = self.printer.get_goal_string(test_data.goal_data)
        expected = "\nWashington goal!\n\nScored by John Carlson with 15:49 remaining in the 2nd period.\n\nWashington: 1\nBoston: 0\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    def test_goal_no_scorer(self):
        actual   = self.printer.get_goal_string(test_data.goal_data_no_scorer)
        expected = ""
        self.assertEqual(expected, actual)


    def test_challenge(self):
        actual   = self.printer.get_official_challenge_string(test_data.challenge_data)
        expected = "\nBoston is challenging the ruling on the play.\n\n#BOSvsWSH #GoAvsGo\n"
        self.assertEqual(expected, actual)


    #################################################
    # Event Replies
    #################################################

    def test_game_scheduled_reply(self):
        previous_data = {}
        actual   = self.printer.get_game_scheduled_reply(previous_data, test_data.game_scheduled_data)
        expected = ""
        self.assertEqual(expected, actual)

    
    def test_game_end_reply(self):
        previous_data = {}
        actual   = self.printer.get_game_end_reply(previous_data, test_data.game_end_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_game_official_reply(self):
        previous_data = {}
        actual   = self.printer.get_game_official_reply(previous_data, test_data.game_official_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_faceoff_reply(self):
        previous_data = {}
        actual   = self.printer.get_faceoff_reply(previous_data, test_data.faceoff_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_stoppage_reply(self):
        previous_data = {}
        actual   = self.printer.get_stoppage_reply(previous_data, test_data.stoppage_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_shot_reply(self):
        previous_data = {}
        actual   = self.printer.get_shot_reply(previous_data, test_data.shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_hit_reply(self):
        previous_data = {}
        actual   = self.printer.get_hit_reply(previous_data, test_data.hit_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_blocked_shot_reply(self):
        previous_data = {}
        actual   = self.printer.get_blocked_shot_reply(previous_data, test_data.blocked_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_giveaway_reply(self):
        previous_data = {}
        actual   = self.printer.get_giveaway_reply(previous_data, test_data.giveaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_takeaway_reply(self):
        previous_data = {}
        actual   = self.printer.get_takeaway_reply(previous_data, test_data.takeaway_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_missed_shot_reply(self):
        previous_data = {}
        actual   = self.printer.get_missed_shot_reply(previous_data, test_data.missed_shot_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_penalty_reply(self):
        previous_data = {}
        actual   = self.printer.get_penalty_reply(previous_data, test_data.penalty_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_ready_reply(self):
        previous_data = {}
        actual   = self.printer.get_period_ready_reply(previous_data, test_data.period_ready_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_start_reply(self):
        previous_data = {}
        actual   = self.printer.get_period_start_reply(previous_data, test_data.period_start_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_end_reply(self):
        previous_data = {}
        actual   = self.printer.get_period_end_reply(previous_data, test_data.period_end_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_period_official_reply(self):
        previous_data = {}
        actual   = self.printer.get_period_official_reply(previous_data, test_data.period_official_data)
        expected = ""
        self.assertEqual(expected, actual)

    
    def test_goal_reply(self):
        previous_data = {}
        actual   = self.printer.get_goal_reply(previous_data, test_data.goal_data)
        expected = ""
        self.assertEqual(expected, actual)


    def test_challenge_reply(self):
        previous_data = {}
        actual   = self.printer.get_official_challenge_reply(previous_data, test_data.challenge_data)
        expected = ""
        self.assertEqual(expected, actual)
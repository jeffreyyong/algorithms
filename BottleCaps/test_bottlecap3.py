import unittest
import sys
from bottlecap3 import *
from contextlib import contextmanager
from io import StringIO


class BottleCapTestCase(unittest.TestCase):
    def setUp(self):
        initial = ["O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"] 
        self.game = BottleCapGame(initial) 

        mid = ["O", "X", "O", "X", "X", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"] 
        self.mid_game = BottleCapGame(mid) 

        final = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"] 
        self.final_game = BottleCapGame(final)

        p1_first_move = ["O", "X", "X", "X", "O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"] 
        self.p2_turn = BottleCapGame(p1_first_move)

        blocked_13_14 = ["O", "X", "X", "X", "O", "O", "O", "X", "O", "O", "O", "X", "O", "X", "X", "X"] 
        self.p2_turn_2 = BottleCapGame(blocked_13_14)

        last_block_1 = ["X", "X", "X", "X", "O", "O", "O", "X", "O", "O", "O", "X", "O", "X", "X", "O"] 
        self.p2_turn_3 = BottleCapGame(last_block_1)


        last_block_2 = ["O", "X", "X", "X", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "X", "O"] 
        self.p2_turn_4 = BottleCapGame(last_block_2)
        

    def test_validate_for_input1(self):
        actual = self.game.validate_for_input([])
        self.assertFalse(actual)

    def test_validate_for_input2(self):
        actual = self.game.validate_for_input([1])
        self.assertTrue(actual)

    def test_input_for_non_crossed(self):
        actual = self.game.validate_for_input([5,6])
        self.assertTrue(actual)

    def test_input_for_crossed(self):
        self.assertFalse(self.game.validate_for_input([2,3]))

    def test_input_more_than_two_apart(self):
        self.assertFalse(self.game.validate_for_input([2,4]))

    
    def test_output_cap_list_player_1(self):
        self.game.output_cap_list("player1")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[91mplayer1\x1b[0m: O_OOOOO_OOO_OOOO')

    def test_output_cap_list_player_2(self):
        self.game.output_cap_list("player2")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[0;32mplayer2\x1b[0m: O_OOOOO_OOO_OOOO')

    def test_output_cap_list_player_1_mid(self):
        self.mid_game.output_cap_list("player1")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[91mplayer1\x1b[0m: O_O__OO_OOO_OOOO')

    def test_output_cap_list_player_2_mid(self):
        self.mid_game.output_cap_list("player2")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[0;32mplayer2\x1b[0m: O_O__OO_OOO_OOOO')

    def test_bot_caps_range_5_to_11(self):
        p1_move_for_5 = self.p2_turn.select_bot_caps([5])
        p1_move_for_6 = self.p2_turn.select_bot_caps([6])
        p1_move_for_7 = self.p2_turn.select_bot_caps([7])
        self.assertEquals(p1_move_for_5, [9])
        self.assertEquals(p1_move_for_6, [10])
        self.assertEquals(p1_move_for_7, [11])

    def test_bot_caps_1(self):
        p1_move_for_1 = self.p2_turn_2.select_bot_caps([1])
        self.assertEquals(p1_move_for_1, [13])

    def test_bot_caps_last_block_one_input(self):
        p1_move_13 = self.game.select_bot_caps([13])
        self.assertEquals(sorted(p1_move_13), [14,15])
        p1_move_14 = self.game.select_bot_caps([14])
        self.assertEquals(sorted(p1_move_14), [15,16])
        p1_move_15 = self.game.select_bot_caps([15])
        self.assertEquals(sorted(p1_move_15), [13,14])
        p1_move_16 = self.game.select_bot_caps([16])
        self.assertEquals(sorted(p1_move_16), [14,15])

    def test_bot_caps_last_block_two_input(self):
        p1_move_13_14 = self.game.select_bot_caps([13,14])
        self.assertEquals(sorted(p1_move_13_14), [15])
        p1_move_14_15 = self.game.select_bot_caps([14,15])
        self.assertEquals(sorted(p1_move_14_15), [13])
        p1_move_15_16 = self.game.select_bot_caps([15,16])
        self.assertEquals(sorted(p1_move_15_16), [14])

    def test_bot_caps_last_block_random(self):
        p1_move_random_last_block_1 = self.p2_turn_3.select_bot_caps([16])
        self.assertEquals(sorted(p1_move_random_last_block_1), [13])
        p1_move_random_last_block_2 = self.p2_turn_3.select_bot_caps([13])
        self.assertEquals(sorted(p1_move_random_last_block_2), [16])
        p1_move_random_last_block_4 = self.p2_turn_4.select_bot_caps([16])
        self.assertEquals(sorted(p1_move_random_last_block_4), [1])

    def test_end_game(self):
        self.assertTrue(self.final_game.end_game())
        self.assertFalse(self.game.end_game())
        
if __name__ == '__main__':
    assert not hasattr(sys.stdout, "gevalue")
    unittest.main(module=__name__, buffer=True, exit=False)

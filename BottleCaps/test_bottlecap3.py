import unittest
import sys
from bottlecap3 import *
from contextlib import contextmanager
from io import StringIO


class BottleCapTestCase(unittest.TestCase):

    def test_validate_for_input1(self):
        actual = validate_for_input([])
        self.assertFalse(actual)

    def test_validate_for_input2(self):
        actual = validate_for_input([1])
        self.assertTrue(actual)

    def test_input_for_non_crossed(self):
        actual = validate_for_input([5,6])
        self.assertTrue(actual)

    def test_input_for_crossed(self):
        self.assertFalse(validate_for_input([2,3]))

    def test_input_more_than_two_apart(self):
        self.assertFalse(validate_for_input([2,4]))

    
    def test_output_cap_list_player_1(self):
        output_cap_list("player1")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[91mplayer1\x1b[0m: O_OOOOO_OOO_OOOO')

    def test_output_cap_list_player_2(self):
        output_cap_list("player2")
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        self.assertEquals(output, '\x1b[0;32mplayer2\x1b[0m: O_OOOOO_OOO_OOOO')
    









if __name__ == '__main__':
    # unittest.main()
    assert not hasattr(sys.stdout, "gevalue")
    unittest.main(module=__name__, buffer=True, exit=False)

    # assert not hasattr(sys.stdout, "getvalue")
    # unittest.main(module=__name__, buffer=False)

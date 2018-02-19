import unittest

from credit_card_checksum import *

class CreditCardTest(unittest.TestCase):

    def test(self):
        actual = is_card_valid("9795526789839145")
        self.assertEqual(actual, False)
        actual = is_card_valid("2861747566959730")
        self.assertEqual(actual, True)
        

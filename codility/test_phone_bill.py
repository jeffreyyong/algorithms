import unittest

from phone_bill import *

class PhoneBillTest(unittest.TestCase):

    def test_phone_bill(self):
        actual = solution("00:01:07,400-234-090")
        self.assertEqual(actual, 201)

        # At least 5 minutes long case
        actual = solution("00:05:00,701-080-080")
        self.assertEqual(actual, 750)
        actual = solution("00:05:01,701-080-080")
        self.assertEqual(actual, 900)


        # All calls to the phone number that ahs the longest total duration of calls are free
        actual = solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090")
        self.assertEqual(actual, 900)


        # All calls to the phone number that has the longest total duration of calls are free
        # In addition to that, if there is a tie, the promotions applies to the phone number
        # with the smallest numerical value
        actual = solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090")
        self.assertEqual(actual, 900)

        actual = solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:05:00,500-234-090\n00:01:07,500-234-090")
        self.assertEqual(actual, 1950)






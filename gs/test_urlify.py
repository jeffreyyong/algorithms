import unittest

from urlify import *

class UrlifyTest(unittest.TestCase):

    def test_urlify(self):

            # data = [
        # (list('much ado about nothing      '), 22,
         # list('much%20ado%20about%20nothing')),
        # (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

        solution = Solution()
        actual = solution.urlify(list('much ado about nothing      '), 22)
        self.assertEqual("much%20ado%20about%20nothing", actual)

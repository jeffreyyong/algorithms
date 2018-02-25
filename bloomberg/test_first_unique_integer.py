import unittest

from first_unique_integer import *

class FirstUniqueIntegerTest(unittest.TestCase):

    def test_first_unique(self):
        actual = solution([3,5,9,2,3,5,1,7,9,7,9])
        self.assertEqual(actual, 2)

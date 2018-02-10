import unittest

from increment_arbitrary_precision_integer import *

class PlusOneTest(unittest.TestCase):

    def test_plus_one(self):

        solution = Solution()
        actual = solution.plus_one([1,2,9])
        self.assertListEqual([1,3,0], actual)

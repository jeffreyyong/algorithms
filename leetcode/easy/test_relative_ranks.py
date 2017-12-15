import unittest

from relative_ranks import *

class RelativeRanksTest(unittest.TestCase):

    def test_relative_ranks(self):

        solution = Solution()
        actual = solution.find_relative_ranks([5,4,3,2,1])
        self.assertEqual(["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"], actual)


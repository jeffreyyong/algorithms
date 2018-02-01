import unittest

from word_ladder import *

class LadderLengthTest(unittest.TestCase):

    def test_ladder_length(self):

        solution = Solution()
        actual = solution.ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        self.assertEqual(5, actual)

import unittest

from count_and_say import *

class CountAndSayTest(unittest.TestCase):

    def test_count_and_say(self):

        solution = Solution()
        actual = solution.count_and_say(1)
        self.assertEqual("1", actual)
        actual = solution.count_and_say(4)
        self.assertEqual("1211", actual)
        actual = solution.count_and_say(5)
        self.assertEqual("111221", actual)

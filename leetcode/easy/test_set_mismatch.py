import unittest

from set_mismatch import *

class SetMistmatchTest(unittest.TestCase):

    def test_set_mismatch(self):

        solution = Solution()
        actual = solution.find_error_nums([1,2,2,4])
        self.assertEqual([2,3], actual)

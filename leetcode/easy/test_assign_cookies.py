import unittest

from assign_cookies import *

class AssignCookiesTest(unittest.TestCase):

    def test_find_content_children(self):

        solution = Solution()
        actual = solution.find_content_children([1,2,3], [1,1])
        self.assertEqual(1, actual)
        actual = solution.find_content_children([1,2], [1,2,3])
        self.assertEqual(2, actual)

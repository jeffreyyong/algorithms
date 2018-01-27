import unittest

from add_binary import *

class AddBinaryTest(unittest.TestCase):

    def test_add_binary(self):

        solution = Solution()
        actual = solution.add_binary("11", "1")
        self.assertEqual("100", actual)

import unittest

from convert_num_to_hex import *

class ToHextTest(unittest.TestCase):

    def test_to_hex(self):

        solution = Solution()
        actual = solution.to_hex(26)
        self.assertEqual("1a", actual)


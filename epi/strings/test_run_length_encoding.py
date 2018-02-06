import unittest

from run_length_encoding import *

class RunLengthEncodingTest(unittest.TestCase):

    def test_decoding(self):

        solution = Solution()
        actual = solution.decoding("3e4f2e")
        self.assertEqual("eeeffffee", actual)


    def test_encoding(self):

        solution = Solution()
        actual = solution.encoding("aaaabcccaa")
        self.assertEqual("4a1b3c2a", actual)

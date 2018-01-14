import unittest

from number_of_segments import *

class NumberOfSegmentsTest(unittest.TestCase):

    def test_number_of_segments(self):

        solution = Solution()
        actual = solution.count_segments("Hello, my name is John")
        self.assertEqual(5, actual)

import unittest

from degree_of_an_array import *

class DegreeOfAnArrayTest(unittest.TestCase):

    def test_degree_of_an_array(self):

        solution = Solution()
        # actual = solution.find_shortest_subarray([1,2,2,3,1])
        # self.assertEqual(2 , actual)
        actual = solution.find_shortest_subarray([1,2,2,3,1,4,2])
        self.assertEqual(6, actual)

import unittest

from intersection_of_two_arrays_ii import *

class IntersectionOfTwoArraysTest(unittest.TestCase):

    def test_intersection_of_two_arrays(self):

        solution = Solution()
        actual = solution.intersect([1,2,2,1], [2,2])
        self.assertEqual([2, 2], actual)

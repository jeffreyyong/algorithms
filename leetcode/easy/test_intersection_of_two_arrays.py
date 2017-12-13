import unittest

from intersection_of_two_arrays import *

class IntersectionOfTwoArraysTest(unittest.TestCase):

    def test_intersection_of_two_arrays(self):

        solution = Solution()
        actual = solution.intersection([1,2,2,1], [2,2])
        self.assertEqual([2], actual)

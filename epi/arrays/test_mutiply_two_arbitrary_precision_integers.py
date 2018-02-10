import unittest

from multiply_two_arbitrary_precision_integers import *

class MultiplyTest(unittest.TestCase):

    def test_multiply(self):

        solution = Solution()
        actual = solution.multiply([1,9,3,7,0,7,7,2,1], [-7,6,1,8,3,8,2,5,7,2,8,7])
        self.assertListEqual([-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7], actual)

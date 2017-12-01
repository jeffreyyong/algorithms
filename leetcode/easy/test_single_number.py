import unittest

from single_number import Solution

class SingleNumberTest(unittest.TestCase):

    def test_single_number(self):
        solution = Solution()
        actual = solution.single_number([1,1,2,2,3])
        self.assertEqual(3, actual)

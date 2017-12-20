import unittest

from happy_number import *

class HappyNumberTest(unittest.TestCase):

    def test_happy_number(self):

        solution = Solution()
        actual = solution.is_happy(19)
        self.assertEqual(True, actual)

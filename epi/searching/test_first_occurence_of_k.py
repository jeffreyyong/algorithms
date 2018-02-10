import unittest

from first_occurence_of_k import *

class TestFirstKTest(unittest.TestCase):

    def test_first_k(self):

        solution = Solution()
        actual = solution.search_first_of_k([-14,-10,2,108,108,243,285,285,401], 108)
        self.assertEqual(3, actual)

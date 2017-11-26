import unittest

from hamming_distance import Solution

class HammingDistanceTest(unittest.TestCase):

    def test_hamming_distance(self):
        solution = Solution()
        actual = solution.hamming_distance(1,4)
        self.assertEqual(2, actual)

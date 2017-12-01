import unittest

from shortest_word_distance import Solution

class KeyboardRowTest(unittest.TestCase):

    def test_shortest_word_distance_1(self):
        solution = Solution()
        actual = solution.shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
        self.assertEqual(3, actual)

    def test_shortest_word_distance_2(self):
        solution = Solution()
        actual = solution.shortest_distance(["practice", "makes", "prefect", "coding", "makes"], "makes", "coding")
        self.assertEqual(1, actual)

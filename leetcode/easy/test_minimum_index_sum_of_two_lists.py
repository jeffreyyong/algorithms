import unittest

from minimum_index_sum_of_two_lists import *

class FindRestaurantTest(unittest.TestCase):

    def test_find_restaurant(self):

        solution = Solution()
        actual = solution.find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
        self.assertEqual(["Shogun"] , actual)

        actual = solution.find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
        self.assertEqual(["Shogun"], actual)


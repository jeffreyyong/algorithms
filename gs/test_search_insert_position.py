import unittest
'''
Example 1:
Input: [1,3,5,6], 5
Ouput: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 1:
Input: [1,3,5,6], 0
Output: 0
'''

from search_insert_position import *

class SearchInsertTest(unittest.TestCase):

    def test_search_insert(self):

        solution = Solution()
        actual = solution.search_insert([1,3,5,6], 5)
        self.assertEqual(2, actual)
        actual = solution.search_insert([1,3,5,6], 2)
        self.assertEqual(1, actual)
        actual = solution.search_insert([1,3,5,6], 7)
        self.assertEqual(4, actual)
        actual = solution.search_insert([1,3,5,6], 0)
        self.assertEqual(0, actual)



    def search_insert(self, nums, target):

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if nums[left] < target:
            return left + 1
        else:
            return left

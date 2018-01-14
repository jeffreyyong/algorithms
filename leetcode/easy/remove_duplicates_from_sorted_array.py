'''
Given a sorted array, remove the duplicates in-place such that each element appear only once
and return the new length.

Do not allocate extra space for another array, you must do thi sby modifying the input arry
in-place with O(1) extra memory

Example:
    Given nums = [1,1,2],
    
    Your function should return length = 2, with the first two elements of nums being 1 and 2 
    respectively and It doesn't matter what you leave beyond the new length
'''

'''
Since the array is already sorted, we can keep two pointers i and new_tail, where new_tail is the
slow_runner while i is the fast-runner. As long as nums[new_tail] = nums[i], we increment
i to skip the duplicate

When we encounter nums[i] != nums[new_tail], the duplicate run has ended so we must copy its value
to nums[new_tail + 1], new_tail is then incremeneted and we repeat the same process again until 
i reached the end of the array.
'''

class Solution:

    def remove_duplicates(self, nums):
        if not nums:
            return 0

        new_tail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]

        return new_tail + 1

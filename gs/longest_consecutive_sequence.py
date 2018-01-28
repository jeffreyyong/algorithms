'''
Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example, given [100,4,200,1,3,2], the longest consecutive elements sequence
should be [1,2,3,4]. It's length is 4

Your algorithm shouuld run in O(n) complexity
'''


'''
Approach #1 Brute Force [Time Limit Exceeded]
Intuition

Because a sequence could start at any number in `nums`, we can exhaust the entire search 
space by building as long a sequence as possible from every number.

Algorithm

The brute force algorithm does not do anything clever - it just considers each number 
in nums, attempting to count as high as possible from that number using 
only numbers in nums. After it counts too high (i.e. currentNum refers to a number that
nums does not contain), it records the length of the sequence if it is larger than the
current best. The algorithm is necessarily optimal because it explores every possibility.

Complexity Anaylsis:

Time complexity O(n^3):
    The outer loop runs exactly n times, and because currentNum increments by 1 during
    each iteration of the `while` loop, it runs in O(n) time. Then, on each iteration of the
    `while` loop, an O(n) lookup in the array is performed. Therefore, this brute force
    algorithm is really three nested O(n) loops, which compound multiplicatively to a cubic
    runtime.
'''

class Solution:

    def longest_consecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    '''
    Approach # Sorting [Accepted]
    Intuition

    If we can iterate over the numbers in ascending order, then it will be easy to find sequences
    of consecutive numbers. To do so, we can sort the array.

    Algorithm

    Before we do anything, we check for the base case input of the empty array. The longest 
    sequence in an empty array is, of course, 0, so we can simply return that. For 
    all other cases, we sort nums and consider each number after the first (because
    we need to compare each number to its previous number). If the current number and 
    the previous are equal, then our current sequence is neither extended nor broken, so
    we simply move on to the next number. If they are unequal, then we must check whether 
    the current number extends the sequence (i.e. nums[i] == nums[i-1] + 1). If it does,
    then we add to our current count and continue. Otherwise, the sequence is broken, 
    so we record our current sequence and reset it to 1 (to include the number that broke 
    the sequence). It is possible that the last element of nums is part of the longest sequence,
    so we return the maximum of the current sequence and the longest one.

    Sorting Example

    [9,1,4,7,3,-1,0,5,8,-1,6] 
                 |
                \/

    [-1,-1,0,1,3,4,5,6,7,8,9]

    Here, an example array is sorted before the linear scan identifies all consecutive sequences.
    The longest sequence is colored in red.

    Complexity Analysis:
        Time complexity O(nlgn):
            The main `for` loop does constant work n times, so the algorithm's time complexity is 
            dominated by the invocation of sort, which will run O(nlgn) time
        Space complexity O(1) (or O(n))
            For the implementations provided here, the space complexity is constant beacse we sort
            the input array in place. If we are not allowed to modify the input array, we must
            spend liear space to store a sorted copy.
    '''

class Solution:


     def longest_consecutive_2(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

'''
Approach #3 HashSet and intelligent sequence building [accepted]

Intuition:
    It turns out that our initial brute force solution was on the right track, but missing
    a few optimizations necessary to reach O(n) time complexity.

Algorithm:
    The optimised algorithm contains only two changes from the brute forec approach: the 
    numbers are stored in a `HashSet` (or `Set` in Python) to allow O(1) lookups, and 
    we only attempt to build sequences from numbers that are not already part of a longer
    sequence. This is accomplished by first ensuring that the number that would immediately 
    precede the current number in a sequence is not present, as that number would
    necessarily be part of a longer sequence.
'''

class Solution:


    def longest_consecutive_3(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

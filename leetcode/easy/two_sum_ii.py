'''
Given an array of integers that is already sorted in ascending order, find two numbers
such that they add up to a specific target number.

The function two_sum should return indices of the two numbers such that they add up to the target
where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
are not zero-based

You may assume that each input would have exactly one solution and you may not use the same element twice.

input: numbers = [2,7,11,15], target = 9
output: index1=1, index2=2
'''

class Solution:

    # two-pointer
    def two_sum_3(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    # dictionary
    def two_sum_1(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num] + 1, i + 1]
            dic[num] = i


    # binary search (slow version)
    def two_sum_2(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]

            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

    # binary search (fast version)
    # Don't repeat investigating the elements that have been already investigated
    # binary search becomes the fastest method
    def two_sum(self, numbers, target):
        investigated_so_far = []
        for i in range(len(numbers)):
            if not numbers[i] in investigated_so_far:
                investigated_so_far.append(numbers[i])
                l, r = i + 1, len(numbers) - 1
                tmp = target - numbers[i]
                while l <= r:
                    mid = l + (r - l) // 2
                    if numbers[mid] == tmp:
                        return([i + 1, mid + 1])
                    elif numbers[mid] < tmp:
                        l = mid + 1
                    else:
                        r = mid - 1

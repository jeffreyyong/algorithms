'''
TODO:

Find the kth largest element in an unsorted array. Note that it is the kth largest element
in the sorted order, not the kth distict element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
'''

class Solution:

    # O(nlogn) time
    def find_kth_largest_1(self, nums, k):
        return sorted(nums, reverse=True)[k-1] 

    # O(nk) time, bubble sort idea, TLE
    def find_kth_largest_2(self, nums, k):
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    # O(nk) time, selection sort idea
    def find_kth_largest_3(self, nums, k):
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]


    # O(k+(n-k)lgk) time, min-heap
    def find_kth_largest_4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def find_kth_largest_5(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]

    # O(n) time, quick selection
    def find_kth_largest(self, nums, k):
        # convert the kth largest to smallest
        return self.find_kth_smallest(nums, len(nums) + 1 - k)

    def find_kth_smallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.find_kth_smallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.find_kth_smallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the righst-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] =  nums[r], nums[low]
        return low

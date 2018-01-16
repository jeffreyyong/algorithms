'''
Given an array of integers and an integer k, find out whether there are two distinct indices i
and j in the array such that nums[i] = nums[j] and the absolute difference between i and j 
is at most k.
'''

class Solution:

    def contains_near_by_duplicate(self, nums, k):
        dic = {}

        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i

        return False

    '''
    Approach #1 (Naive Linear Seach) [Time Limit Exceeded]

    Intuition:
        look for duplicate element in the previous `k` elements

    Algorithms:
        This algorithm is the asme as Approach #1 in Contains Duplicate solution, except that it looks
        at previous `k` elements instead of all its previous elements

        Another perspective of this algorithm is to keep a virtual sliding window fo the previous `k`
        elements. We scan for the duplicate in this window.

    Complexity Analysis:
        Time complexity: O(n min(k, n)). It costs O(min(k,n)) time for each linear search. Apparently we
        do at most `n` comparisons in one search even if `k` is larger than n.

        Space complexity: O(1)
    '''

    def contains_near_by_duplicate_1(self, nums, k):
        for i in range(len(nums)):
            for j in range(max(i - k, 0), i):
                if nums[i] == nums[j]:
                    return True


        return False

    '''
    Approach #2 (Binary Search Tree) [Time Limit Exceeded]

    Intuition:
        Keep a sliding window of `k` elements using self-balancing Binary Search Tree (BST)

    Algorithm:
        The key to improve upon Approach #1 above is to reduce the search time of the previous `k`
        elements. Can w use an auxiliary data strcuture to maintain a sliding window of `k` elements
        with more efficient `search`, `delete` and `insert` operations? Since elements in the sliding 
        window are strictly FIFO, queue is a natural data strcuture. A queue using a linked list 
        implementation supports constant time `delete` and `insert` operations, however the `search`
        costs linear time, which is no better than Approach #1.

        A better option is to use a self-balancing BST. A BST supports `search`, `delete` and `insert`
        operations all in O(log k) time, where `k` is the number of elements in the BST. In most 
        interviews you are not required to implement a self-balancing BST, so you may think of it as 
        a black box. Most programming languages provide implenetations of this useful data structure
        in its standard library. In Java, you may use a `TreeSet` or a `TreeMap`

        If you already have such a data structure available, the pseduocode is:
            Lopp through the array, for each element do 
                - Search current element in the BST, return `true` if found
                - Put current eleemnt in the BST
                - If the size of the BST is larger than `k`, remove the oldest item.

            Return False
    '''


    '''
    Approach #3 (Hash Table) [Accepted]

    Intuition:
        Keep a sliding window of `k` elements using Hash Table

    Algorithm:
        From the previous approaches, we know that even logarithmic performance in `search` is not enough,
        In this case, we need a data structure supporting constant time `search`, `delete` and `insert`
        operations. The algorithm and implementation:

            - Loop through the array, for each element do:
                - Search current element in the HashTable, return True if found
                - Put current element in the HashTable
                - If the size of the HashTable is larger than `k`, remove the oldest item
            - Return False
    '''

    def contains_near_by_duplicate_3(self, nums, k):
        container = set()
        for i in range(len(nums)):
            if nums[i] in container:
                return True
            container.add(nums[i])

            if len(container) > k:
                container.remove(nums[i - k])

        return False

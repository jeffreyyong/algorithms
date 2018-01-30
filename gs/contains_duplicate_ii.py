'''
Given an array of integers and and integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''


'''
Solution

Approach #1 Naive Linear Search [Time limit exceeded]

Intuition:
    Look for duplicate element in the previous k elements.

Algorithm:
    this algorithm is the same as Approach #1 in Contains Duplicate solution.  except that it looks at
    previous k elements instead of all its previous elements

    Another perspective of this algorithm is to keep a virtual sliding window of the previous k elements. 
    We scan for the duplicate in this window.

Complexity Analysis:
    Time complexity O (N min(k,n)). It costs O(min(k,n)) time for each linear search. Apparently we 
    do at most n comparisons in one search even if k can be largeer than n

    Space complexity O(1)
'''

class Solution:

    def contains_near_duplicate(self, nums, k):
        for i in range(len(nums)):
            for j in range(max(i - k, 0), i):
                if nums[i] == nums[j]:
                    return True

        return False


    '''
    Approach #2 Binary Search Tree [Time limit exceeded[

    Intuition:
    Keep a sliding window of k elements using self-balancing Binary Search Tree (BST)

    Algorithm:
    The key to improve upon on Approach #1 above is to reduce the search time of the previous k elements. Can
    we use auxiliary data structure to maintain a sliding window of `k` elements with more efficient `search`,
    `delete` and `insert` operations? Since elements in the sliding window are strictly First-In-First-Out (FIFO),
    queue is a natural data structure. A queue using a linked list implementation suports constant time 
    `delete` and `insert` operations, however the `search` costs linear time, which is no better than Approach #1

    A better option is to use a self-balancing BST. A BST supports `search`, `delete` and `insert` operations all in 
    O(log k) time, where k is the number of elements in the BST. In most interviews you are not required to implement
    a self-balancing BST, so you may think of it as black box. Most programming languages provide implementations of 
    this useful data structure in its standard library. In Java, you may use a TreeSet or a TreeMap

    If you already have such data strucutre availabe the pseudocode is:
        1) Loop through the array, for each element do
            - Search current element in the BST, return True if found
            - Put current element in the BST
            - If the size of the BST is larger than k, remove the oldest item

        2) Return false
    '''



    '''
    Intution:

    Keep a sliding window of k elements using Hash Table

    Algorithm

    From the previous approaches, we know that even logaritmic preformance in `search` is not enough. In thise case, we need
    a data structure supporting constant time search, delete and insert operations. Hash Table is the answer.
    The algorithm and implementation are almost identical to Approach #22


    1) Loop through the array, for each element do:
        - Search current element in the HashTable, return true if found
        - Put current element in the HashTable
        - If the size of the HashTable is larger than k, remove the oldest item.

    2) Return False

    '''

    def contains_near_duplicate_3(self, nums, k):

        num_set = set()

        for i in range(len(num_set)):
            if nums[i] in num_set:
                return True

            num_set.add(nums[i])

            if len(num_set) > k:
                num_set.remove(nums[i - k])

        return False

            

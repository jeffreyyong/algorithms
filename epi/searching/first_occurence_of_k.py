'''
Binary search commonly asks for the index of any element of a sorted array that is equal to a specified 
element. The following problem has a slight twist on this.

-14     -10     2       108     108     243     285     285     285     401
A[0]    A[1]    A[2]    A[3]    A[4]    A[5]    A[6]    A[7]    A[8]    A[9]

Write a method that takes a sorted array and a key and returns the index of the first ocuurence of that key 
in the array. Return -1 if the key does not appear in the array. For example, when appied to the array 
your algorithm should return 3 if the given key is 108; if it is 285, your algorithm should return 6.
'''

'''
Solution:
A naive approach is to use binary search to find the index of any element equal to the key, k (If k is not present, 
we simply return -1). After finding such element, we traverse backwards from it to find the first occurence of that 
element. The binary search takes time O(log n). where `n` is the number of entries in the array. Traversing backwards
takes O(n) time in the worst-case - consider the case where entires are equal to k.

The fundamental idea of binary search is to maintain a set of candidate solutions. For the current problem, if we see the
element at index `i` equals `k`, although we do not know whether `i` is the first element equal to `k`, we do know that
no subsequent elements can be the first one. Therefore we remove all elements with index `i + 1` or or more from the candidates.

Let's apply the logic to the given example, with `k=108`. We start with all indeces as candidates i.e. with [0,9]. The midpoint
index, 4 contains `k`. Therefore we can now update the candidate set to [0,3], and record 4 as an occurence of `k`. The next 
midpoint is 1, and this index contains -10. We update the candidate set to [2,3]. The value at the midpoint 2 is 2. so we update
the candidate set to [3,3]. Since the value at this midpoint is 108, we update the first seen occurence of  `k` to 3.
Now the interval is [3,2], which is empty, terminating the search - the result is 3.
'''

class Solution:

    def search_first_of_k(self, A, k):
        left, right, result = 0, len(A) - 1, -1
        # A[left: right + 1] is the candidate set.
        while left <= right:
            mid = (left + right) // 2
            if A[mid] > k:
                rigth = mid - 1
            elif A[mid] == k:
                result = mid
                right = mid - 1 # Nothing to the right of mid can be solution.
            else: # A [mid] > k
                left = mid + 1
        return result

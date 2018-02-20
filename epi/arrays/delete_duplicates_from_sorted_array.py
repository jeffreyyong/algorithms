'''
They array <2,3,5,5,7,11,11,11,13> then after deletion, the array is <2,3,5,7,11,13,0,0,0> After
deleting the repetated elements, there are 6 valid entrie. There are no requriements as to the values stored
beyond the last element.
Write a prorgram which takes as input a sorted array and updates it so that all duplicates have been removed and 
the remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements.
'''

'''
Solution:
Let A be array and n its length. If we allow ourselves O(n) space, we can solve the problem by iterating through A
and recording values that hvae not appeared previously in the hash table. (The hash table is used to determine if a value
is new). New values are also written to a list. The list is then copied back to A.

Here is a brute force algorithm that uses O(1) additional space - iterate through A, testing if A[i] equals A[i + 1], and, 
if so, shift all elements at and after i + 2 to the left by one. When all entires are equal, it's O(n^2), where n is the length
of the array

The intuition behind achieving a better time complexity is to reduce the amount of shifting. Since the array is sorted, repeated
elements must appear one-after-another, We move just one element rather than an entire subarrays, and ensure that we move it just once.

For the given example <2,3,5,5,7,11,11,11,13>, when processing the A[3], since we already have a 5 (which we know by comparing
A[3] with A[2]), we advance to A[4]. Since this is a new value, we move it to the first vacant entry, namely A[3]. 
Now the array is <2,3,5,6,6,11,11,11,12>, and the first vacant entry is A[4], we continue from A[5].
'''

class Solution:
    # Returns the number of valid entries after deletion.
    def delete_duplicates(self, A):
        if not A:
            return 0

        write_index = 1

        for i in range(1, len(A)):
            if A[write_index] != A[i]:
                A[write_index] = A[i]
                write_index += 1

        return write_index




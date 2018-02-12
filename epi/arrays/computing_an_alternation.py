'''
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the 
property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] .......

Hint: can you solve the problem by making local changes to A?
'''

'''
Solution:
One straightforward solution is to sort A and interleave the bottom and top halves of the array. Alternatively, we could
sort A and then swap the elements at the pairs (A[1], A[2], A[3], A[4])... Both these approaches have the same time 
complexity as sorting namely O(nlogn).

You will soon realize that it is not necessary to sort A to achive the desired configuration, because you could
simply rearrange the elements around the median, and then perform the interleaving Median finding can be performed in time
O(n). 

Finally, you may notice that the desired ordering is very loca, and realize that it is not nececssary to find the median.
Iterating through the array and swapping A[i] and A[i + 1] when i is even and A[i]  > A[i + 1] OR when i is oodd and 
A[i] < A[i + 1] achives the desired configuration
'''

class Solution:

    def compute_alteration(self, A):

        for i in range(len(A)):
            A[i: i + 2] = sorted(A[i: i + 2], reverse=i % 2)

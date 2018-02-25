'''
Given an array of comparable objects, you can find either the min or the max of the elements in the array with
n - 1 comparisons, where n is the length of the array

comparing elements may be expensive e.g. a comparison may invovle a number of nested calls or the elements being compared 
may be long strings. Therefore, it is natural to ask if both the min and max can be computed with less than 2(n - 1) comparisons
required to compute the min and the max independently.

Design an algorithm to find the min and max elements in the array. For example, A=[3,2,5,1,2,4]
should return 1 for the min and 5 for the max

Hint: use the fact that a < b and b < c implies a < c to reduce the number of compares used by the brute-force approach.
'''


'''
Solution: 
The brute-force approach is to compute the min and the max independently i.e. with 2(n - 1) comparison. We can reduce the number
of comparisons by 1 by first computing the min and then skipping the comparison with it when computing the max.

One way to think of the problem is that we are searching for the strongest and weakest player in a group of players, assuming players
are totally ordered. There is no point in looking at any n / 2 matches between disjoint pairs of players. The strongest player will 
come from n/2 winners and the weakest players will come from n/2 losers.

We partition the array into min candidates and max candidates by comparing successive pairs - this will give us n/2 candidates for min and n/2
candidates for max at the cost fo n/2 comparisons. It takes n/2-1 comparisons to find the min from the min candidates and n/2-1
comparisons to find the max from the max candidates, yielding a total of (3n/2 - 2) comparisons.

Naively implemented, the above algorithm need O(n) storage. however, we can implement it in streaming fashion, by maintaining candidate min
and max as we process sucessive pairs. Note that this entials three comparisons for each pair.

For the given example A = [3,2,5,1,2,4] we begin by comparing 3 and 2. Since 3 > 2, we set min to 2 and max to 3. Next, we compare 5 and 1. 
Since 5 > 1, we compare 5 with the current max, namely 3. and update the max to 5. We compare 1 with the current min, namely 2, and update
min to 1. Then we compare 2 and 4. Since 4 > 2, we compare 4 with the current max, namely 5. Since 4 < 5, we do not update max. We 
compare 2 with the current min, namely 1. Since 2 > 1, we do not update min.
'''

import collections

def find_min_max(A):
    MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)


    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    # Process two elements at a time.
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))

    # if there is odd number of elements in the arraym we still need to 
    # comprea the last element with the existing answer.
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )

    return global_min_max

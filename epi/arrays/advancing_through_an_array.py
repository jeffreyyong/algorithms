'''
In particular board game, a player has to try to advance through a sequence of positions. Each position has a nonnegative
integer associated with it, representing the maximum you can advance from the position in one move. You begin at the first position, 
and win by getting to the last position. For example, let A = <3,3,1,0,2,0,1> represent the board game, i.e. the ith entry in A is the 
maximum we can advance through A: take 1 step from A[0] to A[1], then 3 steps, from A[1] to A[4], then 2 steps from A[4] to A[6]
which is the last position. Note that A[0] = 3 >= 1, A[1] = 3 >=3 and A[4] >=2, so all moves are valid. If A instead was <3,2,0,0,2,0,1> 
it would not be possible to advance past position 3, so the game cannot be won.

Write a program which takes an array of n integer, where A[i] denotes the maximum you can advance from index i, and returns whether
it's possible to advance to the last index starting from the beginning of the array.
'''


'''
Solution:
It is natural to try advancing as far as possible in each step. This apporach does not always work, because it potentially skips indices
containing large entries. For example, if A = <2,4,1,1,0,2,3>, then it advances to index 2, which contains a 1, which leads to index 3,
after which it cannot progress. However, advancing to index 1, which contains a 4 let us proceed to index 5, from which we can advance to
index 6.

The above example suggests interating through all entires in A. As we iterate through te array, we track the furthest index we know we can 
advance to. The furthest we can advance form index i is i + A[i]. If, for some i before the end of the array, i is the furthest index that
we have demonstrated that we can advance to, we cannot reach the last index. Otherwise, we reach the end.

For example, if A=<3,3,1,0,2,0,1>, we iteratively compute the furthest we can advance to as 0,3,4,4,4,6,6,7 which reaches the last index, 6.
If A = <3,2,0,0,2,0,1>, we iteratively update the furthest we can advance to as 0,3,3,3,3 after which we cannot advance, so it is not possible
to reach the last index.

The code below implements the algorithm. Note that it is robust with respect to negative entires, since we track the maxium of how far we proved 
we can advance to and i + A[i].
'''


class Solution:

    def can_reach_end(self, A):

        furthest_reach_so_far, last_index = 0, len(A) - 1
        i = 0
        while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
            furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
            i += 1
        return furthest_reach_so_far >= last_index

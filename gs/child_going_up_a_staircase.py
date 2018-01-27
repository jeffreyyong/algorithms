'''
This problem can be broken into subproblem, and it contains the optimal substructure property 
its optimal solution can be constructed efficiently from optimal solution of its subproblems, 
we can use dynamic programming to solve this problem.

Dynamic programming

There are the steps to get the solution incrementally

Base cases:
    if n <= 0, then the number of ways should be zero
    if n == 1, then there is only one way to climb the stair
    if n == 2, then there are two ways to climb the stairs, one is one step, the other one is two steps

    - The key intuition to solve the problem is that given a number of stairs, n, if we know the number
    of ways to get to points [n - 1] and [n - 2] respectively, denoted as n1 and n2, then the total
    ways to get to the point [n] is [n1 + n2]

    Because from the [n - 1] point, we can take one single step to reach [n]. And from [n - 2] point, 
    we could take two steps to get there. There is no overlapping between these two solution sets,
    because we differ in the final step.

    Now, given the above intuition, one can construct an array where each node stores the solution for
    each number n. Or if we look at it close, it is clear that this is basically a fibonacci number,
    with the starting numbers as 1 and 2, instead of 1 and 1.

    Time complexity O(n), single loop upto n is required to calculate nth fibonacci number
    Space complexity O(n) Dynamic programming array is used.
'''

class Solution:

    def climb_stairs(self, n):

        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        # all_ways corresponds to the number of solutions to get to the point [n]
        # one_step_before refers to the number of solutions until the point [n - 1]
        # two_steps_before refers to the number of solution until the point [n - 2]

        # From the point [n - 1], we take one step to reach the point [n]
        # from teh point [n - 2], we take a two-stpes leap to reach the point [n]

        one_step_before = 2
        two_steps_before = 1
        all_ways = 0

        for i in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways

        return all_ways

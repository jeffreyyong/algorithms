'''
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system conneted and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money each house, determine the
maximum amount of money you can rob tonight without alerting the police.
'''

'''
Solution
Approach 1 Dynamic Programming

It could be overwhelming thinking of all possibilities on which houses to rob

A natural way to approach this problem is to work on the simplest case first.

Let us denote that:

    f(k) = largest amount that you can rob from the first k houses.
    Ai = Amount of money at the ith house.

Let us look at the case n = 1, clearly f(1) = A1.

Now, let us look at n = 2, which f(2) = max(A1, A2)

for n = 3, you have basically the following two options:

    1. Rob the third house, and add its amount to the first house's amount
    2. Do not rob the third house, and stick with the maximum amount of the first two houses

    Clearly, you would want to choose the larger of the two options at each step

    Therefore, we could summarise the formuila as following:

        f(k) = max(f(k - 2) + Ak, f(k -1))

    We choose the base case as f(-1) = f(0) = 0, which will greatly simplify our code as you
    can see

    The answer will be calculated as f(n). We could use an array to store and calculate
    the result, but since at each step you only need the previous two maximum values,
    two variables are sufficient

    Complexity analysis:

        Time complexity O(n). Assume that n is the number of houses, the time complexity is 
        O(n)

        Space complexity: O(1)
'''

class Solution:

    def rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

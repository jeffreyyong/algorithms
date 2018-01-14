'''
There is a fence with n posts, each post can be painted with one of the k colours.

You have to paint all the posts such that no more than two adjacent fence posts have
the same colour.

Return the total number of ways you can paint the fence.
'''

'''
Solution:

if n == 1, there would be k-ways to paint
if n == 2, there would be two situations:
    - 2.1 You paint same colour with the previous post: k * 1 ways to paint, named it as `same`
    - 2.2 you paint differently with the previous post: k * (k - 1) ways to paint this way, named
            it as `dif`

So, you can think, if n >= 3, you can always maintain these two situations:
    "You either paint the same colour with the previous one, or differently."

Since there is a rule: "no more than two adjacent fence posts have the same color."

We can further analyse:
- from 2.1, since previous two are in the same colour, next one you could only paint differently, and it
    would form one part of "paint differently" case, in the n == 3 level, and the number of ways to paint
    this way would equal to `same * (k - 1)`.
- from 2.2, since previous two are not the same, you can either paint the same colour this time `(dif * 1)`
    ways to do so, or stick to paint differently `(dif * (k - 1))` times

Here you can conclude, when seeing back from the next level, ways to paint the `same`, or variable same would
equal `dif * 1 = dif`, and ways to paint differently, variable `dif`, would equal to 
`same * (k - 1) + dif * (k -1)`


'''

class Solution:

    def num_ways(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k

        same, dif = k, k * (k - 1)

        for i in range(3, n + 1):
            same, dif = dif, (same + dif) * (k - 1)

        return same + dif



    def num_ways_fastest(self, n, k):

        if n == 0:
            return 0

        if k == 0:
            return 0

        dp1 = k
        dp2 = 0

        for _ in range(n-1):
            dp1, dp2 = (k-1) * (dp1 + dp2), dp1

        return dp1 + dp2

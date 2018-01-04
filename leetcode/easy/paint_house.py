'''
There are a row of n houses, each house can be painted with one of the tree colours:
red, blue, gree. The cost of painting each house with a certain color is different. You have
to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain colour is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost fo paiting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on..
Find the minimum cost of painting all the houses.

All costs are positive integers.
'''

class Solution:

    def min_cost(self, costs):
        if costs is None or len(costs) == 0: return 0
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[n - 1][0], costs[n - 1][1], costs[n - 1][2])


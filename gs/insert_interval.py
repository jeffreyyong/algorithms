'''
Given a set of no-overlapping intervals, insert a new interval into the intervals (merge
if necessary)

You may assume that the intervals were initially sorted acoording to their start times. 
Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2: Example 2:Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]
            This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

'''
Analysis:

In other words, the questions gives a new interval, the task is to insert this new interval into an 
ordered non-overlapping intervals. Consider this the merge case

Idea to solve this problem is quite straightforward:
    1. Insert the new interval according to the start value.
    2. Scan the whole intervals, merge two intervals if necessary.
'''

class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    def insert(self, intervals, new_interval):

        res = []
        if len(intervals) == 0:
            res.append(new_interval)
            return res

        # insert the new interval
        intervals.append(new_interval)
        # sort list accoording to the start value
        intervals.sort(key=lambda x:x.start)

        res.append(intervals[0])
        # scan the list
        for i in range(1, len(intervals)):
            cur = intervals[i]
            pre = res[-1]
            # check if the current interval intersects with the previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end) # merge
            else:
                res.append(cur)

        return res

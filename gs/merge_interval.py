'''
Merge intervals

Given a collection of intervals, merge all overlapping intervals

For example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

'''
Analysis:
To check the intersections between interval [a,b] and [c,d],  there are four cases (equal not shown in the figures):
    a____b
c____d

a____b
     c____d

a_______b
    c___d

   a___b
c_______d

But we can simplify these into 2 cases when checking the smaller (smaller start point) interval with the bigger interval.

For the problem, the idea is simple. First sort the vector according to the start value. Second, scan every interval, 
if it can be merged to the previous one, then merge them, else push it into the result vector.

Note here:
The use of std::sort to sort the vector, need to define a compare function, which need to be static. (static bool myfunc() ) The sort 
command should be like this:  std::sort(intervals.begin,intervals.end, Solution::myfunc); otherwise, it won't work properly.

If using python, the sort function is much easier with the lambda func.
'''

class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        res = []    # result list

        if len(intervals)==0:
            return res

        #sort list according to the start value
        intervals.sort(key=lambda x:x.start)

        res.append(intervals[0])

        #scan the list
        for i in range(1,len(intervals)):
            cur = intervals[i]
            pre = res[-1]

            #check if current interval intersects with previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end) #merge
            else:
                res.append(cur) #insert

        return res

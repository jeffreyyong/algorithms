'''
Given an integer, write a function to determine if it is a power of two.

Follow up:
Could you do it without using any loop / recursion?
'''

'''
Power of 2 means only one bit of n is '1', so use the trick n & (n -1) == 0 to judge
'''

class Solution:

    def is_power_of_two(self, n):
        if n <= 0: return False
        return not (n&(n-1))

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity
'''

'''
Because all trailing 0 is from factors 5 * 2

But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125
have three 5 factors. In the n! oepration, factors 2 is always ample.

So we just count how many 5 factors in all number from 1 to n.
'''

class Solution:
    def trailing_zeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailing_zeroes(n / 5)

    def trailing_zeroes_iterative(self, n):
        count = 0
        while n:
            count += n / 5
            n /= 5
        return count

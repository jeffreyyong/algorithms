'''
Given a positive integer num, write a function which returns True if num is a perfect square
else False

Note: Do not use any built in libaray function such as sqrt.
'''

class Solution:
    def is_perfect_square(self, num):
        if num < 0: return False
        if num <= 1: return True
        n = num/2  # start guessing using n = num/2
        while n*n!= num:
            inc = (num-n*n)/(2*n)
            n += inc
            if -1 <= inc <= 1: break
        if n*n < num: n+=1
        if n*n > num: n-=1
        return n*n == num

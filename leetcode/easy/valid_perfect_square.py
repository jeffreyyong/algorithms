'''
Given a positive integer num, write a function which returns True if num is a perfect square
else False

Note: Do not use any built in libaray function such as sqrt.
'''

class Solution:
    def is_perfect_square(self, num):
        return int(num ** 0.5) == num ** 0.5

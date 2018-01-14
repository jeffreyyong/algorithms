'''
Determine wheter an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie - 1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution:

    def is_palindrome(self, x):

        if x < 0:
            return False

        ranger = 1

        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting wih any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include
1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number


    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
'''

class Solution:

    # Need to check n not in seen, it takes O(N) for a list and only O(1) for a set
    def is_happy(self, n):
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1



    def is_happy_1(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

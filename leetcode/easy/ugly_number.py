'''
Write a programme to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2,3,5
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 77

Note that 1 is typically treated as an ugly number
'''

class Solution:
    def is_ugly(self, num):
        n = num
    
        if n <= 0:
            return False

        if n == 1:
            return True

        while n % 2 == 0 or n % 2 ==0 or n % 5 == 0:
            if n % 2 == 0:
                n = n / 2
                if n == 1:
                    return True

            if n % 3 == 0:
                n = n / 3
                if n == 1:
                    return True

            if n % 5 == 0:
                n = n / 5
                if n == 1:
                    return True

        return False

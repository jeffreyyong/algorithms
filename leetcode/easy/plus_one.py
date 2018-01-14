'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that most significant digit at the head of the list.
'''

'''
Solution:
We're given a list of digits, and the idea is to convert that list to an integer, num
So each digit is multiplied by the proper place value and added to num.
For example, if digits = [3,8,2,5] then on the first iteration 3 is multiplied by 10 to the power of 3,
so this results in 3000, which is added to num. Then 8 is multiplied by 10 ^ 2 and added to num and so on

The last step is to add 1 to num, convert it to a list and return the list.
'''

class Solution:

    def plus_one(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num + 1)]

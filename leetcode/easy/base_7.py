'''
Given an integer, return its base 7 string representation.

Example 1:
    Input: 100
    Outpu: "202"

Example 2:
    Input: -7
    Output: "-10"

'''

class Solution:

    def convert_to_7(self, num):
        if num < 0: return "-" + self.convert_to_7(-num)
        if num < 7:  return str(num)
        return self.convert_to_7(num // 7) + str(num % 7)

    def convert_to_7_1(self, num):
        if num == 0:
            return str(0)

        temp = abs(num)
        ans = ''
        while temp:
            ans += str(temp % 7)
            temp = int(temp / 7)

        if num > 0:
            return ans[::-1]

        else:
            return '-' + ans[::-1]

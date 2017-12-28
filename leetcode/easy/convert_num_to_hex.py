'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two'
complement method is used

Note:
1) All letters in hexadecimal (a-f) must be in lowercase
2) The hexadecimal string must not contain extra leading 0s. If the number is zero, it is 
   represented by a single zero character '0'; otherwise, the first character in the
   hexadecimal string will not be zero character.
3) The given number is guaranteed fo fit within the range of a 32-bit signed integer
4) You must not use any method provided by the library which convers/formats the number to 
    hex directly

Example 1:
    Input: 26
    Output: "1a"

Example 2:
    Input: -1
    Output: "ffffffff"
'''

class Solution:

    def to_hex(self, num):

        if not sum:
            return ""

        if num == 0:
            return "0"

        if num < 0:
            num = ~(0xffffffff ^ num)

        hex = ''

        while num > 0:
            hex = "0123456789abcdef"[num % 16] + hex
            num >>= 4
        return hex


    def to_hex_1(self, num):
        return   ''.join(
                        '0123456789abcdef'[(num >> 4 * i) & 15] 
                        for i in range(8)
                        )[::-1].lstrip('0') or '0'

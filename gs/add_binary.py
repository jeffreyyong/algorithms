'''
Given two binary strings, return their sum (also a binary string)

For example,

a = "11"
b = "1"
return "100"

'''

class Solution:

    def add_binary(self, a, b):

        return bin(int(a, 2) + int(b, 2))[2:]

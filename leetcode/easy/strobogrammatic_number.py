'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees 
(looked at upside down)

Write a function to determine if a number is strobogrammatic. The number is represented 
as a string.

For example, the numbers "69", "88" and "818" are all strobogrammatic
'''


class Solution:

    def is_strobogrammatic(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num) // 2 + 1))

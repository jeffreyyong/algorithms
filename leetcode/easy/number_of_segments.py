'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of 
non-space characters.

Please note that the string does not contain any non-printable characters

Example:
    Input: "Hello, my name is John"
    Output: 5
'''

'''
The Python solution is trivially short because Python' split has a lot of default behaviour that makes
it perfect for this sort of problem. Notably, it returns an empty list when splitting an empty string.
It splits on whitespace by default, and it implicitly trims (strips, in Python lingo) the string
beforehand.

Time complexity: O(n)
All builtin language functionality used here runs in either O(n) or O(1) time, so the entire algorithm
runs in linear time

Space complexity: O(n)
split (in both languages) returns an array/list of O(n) length, so the algorithm uses linear additional
space.
'''

class Solution:

    def count_segments(self, s):
        return len(s.split())

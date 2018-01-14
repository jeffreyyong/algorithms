'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you done modifying the input array in-place, return the new length of the array.

Followup:
Could you solve it using only O(1) extra space?

Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
'''

'''
Solution:
    Taking ["a", "a", "b", "b", "c", "c", "c"] as input, this is what you get after each line:

- flips - [('a', 0), ('b', 2), ('c', 4), (None, 7)]
- chunks - [('a', 2), ('b', 2), ('c', 3)]
- compressed - ['a', '2', 'b', '2', 'c', '3']
lastly, overwrite the original array with compressed.
'''

from functools import reduce
class Solution:

    def compress(self, chars):

        put = 0
        move= 0

        while move < len(chars):
            char = chars[move]
            count = 1
            move += 1
            # move the pointer
            while move < len(chars) and chars[move] == char:
                move += 1
                count += 1
            # if only one character
            if count == 1:
                chars[put] = char
                put += 1
            # If more than one character
            else:
                chars[put] = char
                put += 1
                count = str(count)
                for c in count:
                    chars[put] = c
                    put += 1
        return put

'''
Run length encoding (RLE) compression offeres a fast way to do efficient on-the-fly compression
and decompression of strings. The idea is simple - encode successive repeated characters by the reptition
count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The decoding of 
"3e4f2e" returns "eeeffffee"

Implement the run length encoding and decoding functions. Asusme the string to be encoded consists of 
letters of the alphabet, with digits, and the string to be decoded is a valid encoding.

hint: This is similar to converting between binary and string representations
'''

'''
Solution: 
First we consider the decoding function. Every encoded string is a repetition of a string of digits
followed by a single character. The string of digits is the decimal representation of a positive 
integer. To generate the decoded sting, we need to convert this sequence of digits into its integer
equivalent and then write the characvter that many times. We do this for each character. 

The encoding function requires an integer (the repetition count) to string conversion.
'''

class Solution:

    def decoding(self, s):

        count, result = 0, []
        for c in s:
            if c.isdigit():
                count = count * 10 + int(c)
                print("count", count)
            else: # c is a letter of alphabet
                result.append(c * count) # Appends count copies of c to result.
                count = 0
        return ''.join(result)


    def encoding(self, s):

        result, count = [], 1
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[i - 1]:
                # Found new character to write the count of previous character.
                result.append(str(count) + s[i - 1])
                count = 1
            else: # s[i] == s[i - 1]
                count += 1

        return ''.join(result)

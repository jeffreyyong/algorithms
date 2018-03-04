'''
Given a string containing a set of words separated by whitespace, transform it to a string in which the words appear
in the reverse order. For example, "Alice likes Bob" transforms to "Bob likes Alice". Do not need to keep the original string.

Implement a function for reversing the words in a string s.

Hint: It's difficult to solve this with one pass.
'''

'''
Solution:

The code for computing the position for ecah character in the final result in a single pass is intricate
However, for the special case where each word is a single character, the desired result is simply the reverse of s.

For the general case, reversing s gets the wrods to their correct relative positions. However, for words that are larger
than one character, their letters appear in reverse order. This situation can be corrected by reversing the individual words.

For example, "ram is costly" reversed yields "yltsoc si mar". We obtain the final result by reversing each worrd to obtain 
"costly is ram".
'''
# Seems like there is a bug in the book
# Assume s is a string encoded as bytearray.

def reverse_words(s):
    # First, reverse the whole string
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1


    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break

        # Reverses each word in the string
        reverse_range(s, start, end - 1)
        start = end + 1

    # Reverses the last word.
    reverse_range(s, start, len(s) - 1)

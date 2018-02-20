'''
Taking a string (the "sentence" string) and a set of strings (the "words"), and finding the subsstrings of the sentence which
are the contcatentation of all the words (in any order). For example, if the sentence string is "amanaplanacanal" and the set of words
is ["can", "apl", "ana"], "aplanacan" is a substring of the sentence that is the concatenation of all the words

Write a program which takes as input a string (the "sentence") and an array of srtings (the "words"), and returns the starting
indicies of substrings of the sentence string which are the concatentation of all the strings in the words array. Each string
must appear exactly once, and their ordering is immaterial. Assume all strings in the worrds array have equal length. It is possible
for the words array to contain duplicates.

Hint: exploit the fact that the words have the same length.

Solution: Let's begin by considering the problem of checking whether a string is the concatenation strings in words. We can solve this 
problem recursively - we find a string from words that is a prefix of the given string, and recurse with the remaining words and the 
remaining suffix. 

When all strings in words have equal length, say n, only one distict string in words can be a prefix of the given string. So we can directly
check the first n characters of the string to see if they are in words. If not, the string cannot be the concatenation of words. If it is, 
we remove that string from words and continue with the remainder of the string and the remaining words. 

To find substrings in the sentence string that are the concatenation of the strings in words, we can use the above process for 
each index in the sentence as the starting index.

Time complexity: 

Let m be the number of words and n the length of each word. Let N be the length of the sentence. For any fixed i, to check if the string of length
nm starting at an offset of i in the sentence is the concatenation of all words has time complexity O(nm), assuming a hash table is used
to store the set of words. This implies the overall time complexity is O(Nnm). In practice, the individual checks are likely to be much faster
becuse we can stop as soon as a mismatch is detected.

The problem is made easier, complexity-wise and implementation-wise, by the fact that the words are all the same length - it makes testing
if a substring equals the concatenation of words straightforward.
'''

import collections

def find_all_substrings(s, words):

    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()

        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i: i + unit_size]
            it  = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be possible.
                return False
            return True

        word_to_freq = collections.Counter(words)
        unit_size = len(words[0])
        return [
            i for i in range(len(s) - unit_size * len(words) + 1)
            if match_all_words_in_dict(i)
        ]

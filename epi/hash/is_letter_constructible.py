'''
Write a program which takes text for an anonymous letter and text for a magazine and determines if it is 
possible to write the anonymous letter using the magazine. The anonymous letter can be written using the magazine
if for each character in the anonymous letter, the number of times it appears in the anonymous letter is no 
more than the number of times it appears in the magazine.

Hint: Count the number of distinct characters appearing in the letter.
'''

'''
Solution: A brute force approach is to count for each character in the character set the number of times it appears in the 
letter and in the magazine. If any characters ocrurs more often in the letter than the magazine we return false, 
otherwise we return true. This approach is potentially slow because it iterates over all characters, including those 
that do not occur in the letter of magazine. It also makes multiple passes over both the letter and the magazine -
as many passes as there are characters in the character set.

A better approach is to make a single pass over the letter, storing the character counts for the letter in a single hash 
table - keys are characters,  and values are the number of times that character appears. Next, we make a pass
over the magazine. When processing a character `c`, if `c` appears in the hash table, we reduce its count by 1; we remove it from 
the hash when its count goes to zero. If the hash becomes empty, we return true. If we reach the end of the letter and the hash
is nonempty. We return false - each of the characters remaining in the hash occurs more time in the letter than the magazine.

In the worst-case, the letter is not constructible or the last character of the magazine is essentially required. Therefore, the
time complexity is O(m + n) where m and n are the number of characters in the letter and magazine, respectively. The space complexity
is the size of the hash table constructed in the pass over the letter i.e. O(L). where L is the number of distinct characters
appearing in the letter.

If the characters are coded in ASCII, we could do away with the hash table and use a 256 entry integer array A, with A[i] being
set to the number of times the character i appears in the letter.
'''

import collections

class Solution:

    def is_letter_constructible_from_magazine(self, letter_text, magazine_text):
        # Compute the frequencies for all chars in the letter_text
        char_frequency_for_letter = collections.Counter(letter_text)

        # Checks if characters in magazine_text can cover characters in 
        # char_frequency_for_letter

        for c in magazine_text:
            if c in char_frequency_for_letter:
                char_frequency_for_letter[c] -= 1
                if char_frequency_for_letter[c] == 0:
                    del char_frequency_for_letter[c]
        # Empty char_frequency_for_letter means every char in letter_textr can be covered by a char
        # in magazine_text

        return not char_frequency_for_letter




    # Pythonic solution that exploits collections.Counter. Note that the subtraction only keeps
    # keys with positive counts.

    def is_letter_constructible_from_magazine_pythonic(self, letter_text, magazine_text):
        return (not collections.Counter(letter_text) - collections.Counter(magazine_text))


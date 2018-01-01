'''
Given a list of words, return the words that can be typed using letters of alphabet on 
only one row's of American keyboard

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet
'''

import re

class Solution:

    def find_words(self, words):    
        res = []
        set1 = set(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"])
        set2 = set(["a", "s", "d", "f", "g", "h", "j", "k", "l"])
        set3 = set(["z", "x", "c", "v", "b", "n", "m"])

        for word in words:
            set_to_check = None
            char = word[0].lower()
            if char in set1:
                set_to_check = set1
            elif char in set2:
                set_to_check = set2
            elif char in set3:
                set_to_check = set3

            # if not set_to_check:
            #     continue

            failed = False
            for c in word:
                if c.lower() not in set_to_check:
                    failed = True
                    break

            if not failed:
                res.append(word)

        return res

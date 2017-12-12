'''
Given an arbitrary ransom note string and another string containing letters fmor all the 
magazines, write a function that will return true if the ransom note can be constructed
from the magazine; otherwise, it will return false,

Each letter in the magazine string can obly be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution:
    def can_construct(self, ransom_note, magazine):
        return not collections.Counter(ransom_note) - collections.Counter(magazine)

    # O(m+n) with m and n being the lengths of the strings

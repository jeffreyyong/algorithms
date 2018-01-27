'''
Write a method to decide if two strings are anagrams or not
If a one string is a permutation of another string
'''

'''
Solution:
1) Sort the two strings and compare (not the best)
2) If there's one small capital, just small capital all of them then do it
'''

class Solution:

    def anagram(self, str1, str2):
        if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
            return True
        else:
            return False

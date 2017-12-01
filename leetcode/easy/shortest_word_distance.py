'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:

    def shortest_distance(self, words, word1, word2):
        size = len(words)
        index1, index2 = size, size
        ans = size

        for i in range(size):
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1 - index2))

            if words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1 - index2))

        return ans



    # O(n) time, O(1) space.

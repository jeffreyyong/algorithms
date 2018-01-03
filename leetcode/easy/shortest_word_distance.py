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

        def minDis(s1, s2):

            # find the min difference (absolute) between elem in s1 and s2 (both sorted).

            # saddleback search
            i, j = 0, 0
            dist = s1[i] - s2[j]
            dist_min = abs(dist)

            while i < len(s1) and j < len(s2):
                dist = s1[i] - s2[j]
                dist_min = min(dist_min, abs(dist))

                if dist == 0:
                    return 0

                elif dist > 0:
                    j += 1
                else:
                    i += 1

            return dist_min


        idxs_1 = []
        idxs_2 = []

        for i, x in enumerate(words):
            if x == word1:
                idxs_1.append(i)
            if x == word2:
                idxs_2.append(i)


        return minDis(idxs_1, idxs_2)


    

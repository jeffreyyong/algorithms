'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of 
shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''

'''
Solution:

The idea behind it is to use character floping plus bidirectional BFS. Use
set operations as much as possible
'''

import string

class Solution:

    def ladder_length(self, begin_word, end_word, word_dict):

        if end_word not in word_dict:
            return 0
        length = 2
        front, back = set([begin_word]), set([end_word])
        word_dict = set(word_dict)
        word_dict.discard(begin_word)
        while front:
            # generate all valid tranformations

            front = word_dict & (set(word[:index] + ch + word[index + 1:] for word in front
                                     for index in range(len(begin_word)) for ch in string.ascii_lowercase))

            if front & back:
                # there are common elements in front and back, done
                return length

            length += 1

            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating next_set)
                front, back = back, front
            # remove transformations from word_dict to avoid cycle
            word_dict -= front

        return 0


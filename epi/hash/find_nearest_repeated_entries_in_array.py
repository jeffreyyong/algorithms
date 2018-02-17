'''
Write a program which takes as inpyu an array and finds the distance bewteen a closest pair of equal entries
For exmaple, if s = ["All, "work", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
Then the second and third occurences of "no" is the closest pair.

Hint: Each entry in the array is a candidate.
'''

'''
Solution: The brute force approach is to iterate over all pairs of entries, check if they are the same, and if
so, if the distance between them is less than the smalles such distance seen so far. The time complexity is
O(n^2), where n is the array length.

When examining an entry, do not need to look at every entry - only care about entries which are the same. We can store
the set of indices corresponding to a given value using a hash table and iterate over all such sets. 

There is a better approach, when processing an entry, all we care about is the closest previous equal entry. Specifically,
as we scan through the array, for each value seen so far, we store in a hash table the latest index at which it 
appears. When processing the element, we use the hash table to see the latest index less than the current index
holding the same value.

For the given example, when processing the element at index 9, which is "no", the hash table tells us the most recent 
previous occurence of "no" is at index 7, so we update the distance of the closest pair of equal entries seen so
far to 2.

Time complexity:

O(n), since we perform a constant amount of work per erntry. The space complexity is O(d), where d is the number of distinct 
entries in the array.
'''

class Solution:

    def find_nearest_repition(self, paragraph):
        word_to_latest_index, nearest_repeated_distance = {}, float('inf')
        for i, word in enumerate(paragraph):
            if word in word_to_latest_index:
                latest_equal_word = word_to_latest_index[word]
                nearest_repeated_distance = min(nearest_repeated_distance,
                                                 i - latest_equal_word)

            word_to_latest_index[word] = i 

        return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1

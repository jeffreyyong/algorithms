'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of 
favorite restaurants represented by strings

You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:

    The length of both lists will be in the range of [1, 1000].
    The length of strings in both lists will be in the range of [1, 30].
    The index is starting from 0 to the list length minus 1.
    No duplicates in both lists.
'''

'''
Answer:
Say the lists are list1 and list2. Let list1_index[element] be the index of that element in A
for every index, value pair(j, v) in list2, we have some candidate sum-of-indexes i + j,
where i = list1_index[v] if it exists.
If the candidate sum is better, it becomes our new answer, if the candidate sums are the same
then we append to our answer.
'''


class Solution:
    def find_restaurant(self, list1, list2):
        list1_index = {u: i for i, u in enumerate(list1)}
        best, ans = 1e9, []

        for j, v in enumerate(list2):
            i = list1_index.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)

        return ans




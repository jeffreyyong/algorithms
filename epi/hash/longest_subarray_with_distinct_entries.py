'''
Write a program that takes an array and returns the length of a longest subarray with the property that all its elements are distinct. 
For example, if the array is ['f','s','f','e','t','w','e','n','w','e'], then a longest subarray all of whose elements are distinct is
['s','f','e','t','w']

Hint: What should you do if the subarray from indices i to j satisfies the property, but the subarray from i to j + 1 does not?
'''

'''
Solution: 
We begin with a brute force approach. For each subarray, we test if all its elements are distinct using a hash table. The time 
complexity is O(n^3), where n is the array length since there are O(n2) subarrays, and their average length is O(n).


Can improve on the brute-force algorithm by noting that if a subarray contains duplicates, every array containing that subarray
will also contain duplicates. Therefore, for any given starting index, we can compute the longest subarrays starting at that 
index containing no duplicates in time O(n), since we can incrementally add elements to the hash table of elements from the 
starting index. This leads to an O(n^2) algorithm. As soon as we get a duplicate, we cannot find longer beginning at the
same initial index that is duplicate-free.

Can improve the time complexity by reusing previous computation as we iterate through the array. Suppose we know the longest duplicate-free
subarray ending at a given index. The longest duplicate-free subarray ending at the next index is  either the previous subarray appended
with the element at the next index, if that element does not appear in the longest duplicate-free subarray at the current index. Otherwise it is the 
subaarray beginnign at the most recent occurence of the element at the next index to the next index. To perform this case analysis as we iterate
wall we need is a hash table storing the most recent occurence of each element, and the longest duplicate-free subarray ending
at the current element

For the given example, ['f','s','f','e','t','w','e','n','w','e'], when we process the element at index 2, the longest duplicate-free subarray
ending at index 1 is from 0 to 1. The hashtable teslls us that the element at index 2, namely f, appears in that subarray, so we update
the longest subarray ending at index 2 to being from index 1 to 2. Indices 3-5 introduce fresh elements. Index 6 holds a repeated value e, 
which appears within the longest subarray ending at index 5; specifically, it appears at index 3. Therefore, the longest
subarrray ending at index 4 and ends at 6.

Time complexity is O(N), since we perform a constant number of operations per element
'''

def longest_subarray_with_distinct_entries(A):
    # Records the most recent occurrences of each entry.
    most_recent_occurrence = {}

    longest_dup_free_subarray_start_idx = result = 0
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1

        most_recent_occurrence[a] = i

    return max(result, len(A) - longest_dup_free_subarray_start_idx)




'''
Write a program which takes as input a set of integers represented by an array, and returns the size of a large subset
`of integers in the array having the property that if two integers are in the subset, then so are all integers between them.
For example, if th einput is [3,-2,7,9,8,1,2,0,-1,5,8], the largest such subset is [-2,-1,0,1,2,3], so you should return 6.

Hint: Do you really need a totla ordering on the input?
'''

'''
Solution:

The brute-force algorithm is to sort the array and then iterate through it, recording for each entry the largest subset
with the desired property ending at that entry.

Actually, don't need sortind and don't need the total ordering All we care about is whether the integers adjacent to a given
value are present. Can use hash table to store the entries. 

Iterate over the entires in the array, if an entry e is present in the hash table, we compute the largest interval including 
e such that all values in the interval are contained in the hash table. Iteratively searching entires in the hash table of the form
e + 1, e + 2,...., and e - 1, e - 2,.... When we are done, to avoid doing duplicated computation, we remove all the entries
in the computed interval from the hash table, since all these entries are in the same largest contained interval


Example: 
Consider A = [10,5,3,11,6,100,4]. We initialize the hash table to {6,10,3,11,5,100,4}. The first entry in A is 10, and we find the 
largest interval contained in A including 10 by expanding from 10 in each direction by doing lookups in the hash table. The largest 
set is {10,11} and is of size 2. This computation updates the hash table to {6,3,5,100,4}. The next entry in A is 5. Since it 
is contained in the hash table, we know that the largest interval contained in A including 5 has not been computed yet. Expanding from 5,
we see that 3,4,6 are all in the hash table, and 2 and 7 are not in the hash table, so the largest set containing 5 is {3,4,5,6}, which is of size
4. We update the hash table to {100}. The three entries after 5, namelyu 3,11,6 are not present in the hash table, we know we have 
already computed the longest intervals in A containing each of these. Then we get to 100, which cannot be extended, so the largest set 
containing it is {100}, which is of size 1. We update the hash table to {}. Since 4 is not in the hash table, we can skip it. 
The largest of the three sets is {3,4,5,6} 

Time complexity: O(n), where n is the array length, since we add and remove array elements in the hash table no more than once.
'''

def longest_contained_range(A):
    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of th elargest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)


    return max_interval_size

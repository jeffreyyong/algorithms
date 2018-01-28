'''
Givern an array of integers, find if the array contains any duplicates. Your function should return true
if any value appears at least twice in the array, and it should return fales if every element
is distinct
'''

class Solution:

    '''
    For an array of n integres, there are n(n+1)/2 pairs of integers. Thus, we may check all n(n+1)/2 pairs and 
    see if there is any pair with duplicates

    Algorithm:
    To apply this idea, we employ the linear search algorithm which is the simplest search algorithm. Linear search
    is a method of finding if a particular value is in a list by checking each of its elements, one at a time and in 
    sequence until the desired one is found.

    For our problem, we loop through all n integers. For the ith integers nums[i], we search in the previous i - 1
    integers for the duplicate of nums[i]. If we find one, we return true; if not, we contiue. Return false at the 
    end of the programme.

    To prove the correctness of the algorithm, we define the loop invariant. A loop invariant is a property that hodls before
    (and after) each iteration. Knowing its invariant(s) is essential for understanding the effect of the loop. Here is the
    loop invariant: 
            
            Before the next search, there are no duplicate integers in the searched integers

    The loop invariant holds true before the loop because there is no searched interger. Each time through the loop we look 
    for any possible duplicate of the current element. If we found a duplicate, the function exits by returning true;
    if not, the invariant still holds true.

    Therefore, if the loop finishes, the invariant tells us that there is no duplicate in all n integers.

    Complexity Analysis:
        Time complexity:
            O(n^2). In the worst case, ther are n(n+1)/2 pairs of integers to check.

        Space complexity:
            O(1). We only used constant extra space.
    '''

    def contains_duplicate(self, nums):

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    return True


        return False


    '''
    Approach #2 (Sorting) [Accepted]

    Intuition:
        If there are any duplicate integers, they will be consecutive after sorting.

    Algorithm:

    This approach employs sorting algorith. Since comparison sorting algorithm like heapsort is known to provide
    O(n logn) worst-case performance, sorting is often a good preprocessing step. After sorting, we can sweep
    the sorted array to find if there are any two consecutive duplicate elements.
    
    Complexity Analysis:

        Time complexity:
            O(n logn). Sorting is O(n logn) and the sweeping is O(n). The entire algorithm is dominated by the 
            sorting step, which is O(n logn)

        Space complexity:
            O(1). Space depends on the sorting implementation which, usually, costs O(1) auxiliary space if `heapsort` 
            is used.

    '''

    def contains_duplicate_2(self, nums):

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


    '''
    Approach #3 (Hash Table) [Accepted]

    Intuition:
    Utilize a dynamic data structure that supports fast search and insert oprations.

    Algorithm:
    Search operations is O(n) in an unsorted array. Utilizing a data structure with faster search time will speed up the 
    entire algorithm

    The operations we need to support here are `search()` and `insert()`. For a self balancing Binary Seaerch Tree (TreeSet
    or TreeMap in Java), `search()` and `insert()` are both O(logn) time. For a HashTable (HashSet or HashMap) in Java, 
    `search()` and `insert()` are both O(1) on average. Therefore, by using hash table, we can achieve linear time complexity
    for finding the duplicate in an unsorted way.

    Time complexity: O(n), we do `search()` and `insert()` for n times and each operation takes constant time.

    Space complexity O(n). The space used by a hash table is linear with the number of elements in it.

    Note

    For certain test cases with not very large n, the runtime of this method can be slower than Approach #2. The reason is
    hash table has some overhead in maintaining its property. One should keep in mind that real word performance can be 
    different from what the Big-O notation says. The Big-O notation only tells us that for sufficiently large input, one will be faster
    than other. Therefore, when n is not sufficiently large, an O(n) algorithm can be slower than O(n logn) algorithm.
    '''

    def contains_duplicate_3(self, nums):
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)

        return False


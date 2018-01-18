'''
Given an unsorted array of inegers, sort the array into a wave lika array. An array `arr[0...n-1]` is sorted
in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ....

Examples:

    Input: arr[] = {10,5,6,3,2,20,100,80}
    Output: arr[] = {10,5,6,2,20,3,100,80} OR
                    {20,5,10,2,80,6,100,3} OR
                    any other array that is in wave form
'''

class Solution:
    '''
    Solution:

    #Approach 1

    A simple solution is to use sorting. First sort the input array, then swap all adjacent elements. For example,
    let the input array be {3,6,5,10,7,20}. After sorting, we get {3,5,6,7,10,20}. After swapping adjacent elements,
    we get {5,3,7,6,20,10}

    Time complexity: O(nlogn)
    Sorting algorithm like Merge Sort, Heap Sort is used
    '''

    def sort_in_wave_1(self, arr, n):
        # sort the array
        arr.sort()

        # swap adjacent elements
        for i in range(0, n-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    '''
    # Approach 2:
    can be done in O(n) time by doing a single traversal of given array. The idea is based
    on the fact that if we make sure that all even positioned (at index 0,2,4..) elements
    are greater than their adjacent odd elements, we don't need to worry about odd positioned
    element. Following are simple steps.
    1) Traverse all even positioned elements of input array and do following.
        a) If current element is smaller than previous odd element, swap previous and current.
        b) If current element is smallar than next odd element, swap next and current.
    '''

    def sort_in_wave_2(self, arr, n):

        # Traverse all even elements
        for i in range(0, n, 2):

            # If current even element is smaller than previous
            if i > 0 and arr[i] < arr[i -1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

            # If current even element is smaller than next
            if i < n-1 and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr

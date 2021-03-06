'''


A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Assume that:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).



Complexity:

expected worst-case time complexity is O(N);

expected worst-case space complexity is O(1)
Execution:

Sum all elements that should be in the list and sum all elements that actually are in the list. The sum is 0 based, so +1 is required. The first solution using the + operator can cause int overflow in not-python languages. Therefore the use of a binary XOR is adequate.
'''


def solution(A):
    should_be = len(A) # you never see N+1 in the iteration
    sum_is = 0

    for idx in xrange(len(A)):
        sum_is += A[idx]
        should_be += idx+1

    return should_be - sum_is +1

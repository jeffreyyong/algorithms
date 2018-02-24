/*
This is a demo task.

Write a function:

func Solution(A []int) int

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
*/

package counting_elements

func findMissingInteger(A []int) int {
	init := 1
	seen := make(map[int]bool)

	for _, value := range A {
		if value > 0 && !seen[value] {
			seen[value] = true
		}
	}

	for i := init; i <= len(seen); i++ {
		if !seen[init] {
			return init
		}
		init += 1
	}

	return init
}

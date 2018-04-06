/*
Problem: Given array A consisting of N intergers, return the reversed array.
Solution: We can iterate over the first half of the array and exchange the elements with
				  those in the second part of the array.
*/

package iterations

func Sum(x, y int) int {
	return x + y
}

func reverse(A []int) []int {
	N := len(A)

	for i := 0; i < N/2; i++ {
		k := N - i - 1
		A[i], A[k] = A[k], A[i]
	}
	return A
}

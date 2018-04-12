/*
Given a non-negative integer N, returns the largest number in the family of N.
*/

package assessment

import (
	"sort"
	"strconv"
	"strings"
)

func Solution(N int) int {
	str := strconv.Itoa(N)
	strSlice := strings.Split(str, "")
	sort.Sort(sort.Reverse(sort.StringSlice(strSlice)))
	strResult := strings.Join(strSlice, "")
	result, _ := strconv.Atoi(strResult)
	return result
}

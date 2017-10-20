package main

import (
	"fmt"
	"sort"
)

type ByFirstDigit []int

func (s ByFirstDigit) Len() int {
	return len(s)
}

func (s ByFirstDigit) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s ByFirstDigit) Less(i, j int) bool {
	return s[i][0] < s[j][0]
}

// always favour the one with only one digit,
// If there's a second digit, compare the second digit,

// func findLargest(numArray []int) {
// 	sort.Sort(sort.Reverse(sort.IntSlice(numArray)))

// 	// [980 90 10 9 6]
// 	// [998090610]

// 	for _, num := range numArray {
// 		sortedArray := []int{}

// 	}

// }

func main() {
	numArray := []int{9, 980, 10, 6, 90}

	sort.Sort(ByFirstDigit(numArray))
	fmt.Println(numArray)
}

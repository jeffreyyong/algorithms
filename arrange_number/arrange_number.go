package main

import (
	"fmt"
	"sort"
	"strconv"
)

// By first digit

type ByFirstDigit []int

func (s ByFirstDigit) Len() int {
	return len(s)
}

func (s ByFirstDigit) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s ByFirstDigit) Less(i, j int) bool {
	var ii int
	for ii = s[i]; ii >= 10; ii = ii / 10 {
	}
	var jj int
	for jj = s[j]; jj >= 10; jj = jj / 10 {
	}
	return ii < jj
}

// By second digit

type BySecondDigit []int

func (s BySecondDigit) Len() int {
	return len(s)
}

func (s BySecondDigit) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s BySecondDigit) Less(i, j int) bool {
	var ii int
	for ii = s[i]; ii >= 100; ii = ii / 100 {
	}
	var jj int
	for jj = s[j]; jj >= 100; jj = jj / 100 {
	}
	return ii < jj
}

// By third digit

type ByThirdDigit []int

func (s ByThirdDigit) Len() int {
	return len(s)
}

func (s ByThirdDigit) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s ByThirdDigit) Less(i, j int) bool {
	var ii int
	for ii = s[i]; ii >= 1000; ii = ii / 1000 {
	}
	var jj int
	for jj = s[j]; jj >= 1000; jj = jj / 1000 {
	}
	return ii < jj
}

func main() {
	numArray := []int{9, 980, 10, 6, 90}
	fmt.Println(numArray)
	sort.Sort(ByFirstDigit(numArray))
	fmt.Println(createLargest(numArray))
}

func createLargest(numArray []int) map[string][]int {
	numberMap := make(map[string][]int)

	for _, num := range numArray {

		numKey := string(strconv.Itoa(num)[0])

		if numberMap[numKey] == nil {
			numberMap[numKey] = []int{num}
		} else {
			numberMap[numKey] = append(numberMap[numKey], num)
		}
	}

	// Sort by second digit

	for _, numArray := range numberMap {
		if len(numArray) != 1 {
			sort.Sort(BySecondDigit(numArray))
		}
	}

}

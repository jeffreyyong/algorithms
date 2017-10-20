package main

import (
	"reflect"
	"testing"
)

var shiftWordTests = []struct {
	description string
	cipherText  string
	shift       int
	shiftedText string
}{
	{"Forward shift", "ABCD", 2, "CDEF"},
	{"Forward shift", "CDEF", -2, "ABCD"},
	{"Wrapping around Z", "WXYZ", 1, "XYZA"},
	{"Wrapping around Z negative", "XYZA", -1, "WXYZ"},
}

func TestShiftingWord(t *testing.T) {
	for _, tt := range shiftWordTests {
		t.Run(tt.description, func(t *testing.T) {
			expected := tt.shiftedText
			actual := shiftWord(tt.cipherText, tt.shift)

			if expected != actual {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

var splitByLenTests = []struct {
	description  string
	words        []string
	groupedWords map[int][]string
}{
	{"Normal group", []string{"cat", "bat", "bate", "hate"}, map[int][]string{3: []string{"cat", "bat"}, 4: []string{"bate", "hate"}}},
	{"Group with empty string", []string{"", "bate", "hate"}, map[int][]string{0: []string{""}, 4: []string{"bate", "hate"}}},
}

func TestSplittingByLen(t *testing.T) {
	for _, tt := range splitByLenTests {
		t.Run(tt.description, func(t *testing.T) {
			expected := tt.groupedWords
			actual := splitByLen(tt.words)

			if !reflect.DeepEqual(expected, actual) {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

var findCommonTests = []struct {
	description string
	slice1      []int
	slice2      []int
	commonSlice []int
}{
	{"Find common", []int{1, 2, 5, 4}, []int{1, 5, 6, 7}, []int{1, 5}},
	{"No common returns empty slice", []int{1, 2, 5, 4}, []int{9, 9, 9, 9}, []int{}},
}

func TestFindingCommon(t *testing.T) {
	for _, tt := range findCommonTests {
		t.Run("", func(t *testing.T) {
			expected := tt.commonSlice
			actual := findCommon(tt.slice1, tt.slice2)

			if !reflect.DeepEqual(expected, actual) {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

var getAllowedShiftsTests = []struct {
	dictionary    []string
	cipherText    string
	allowedShifts []int
}{
	{[]string{"ABC", "DEF", "GHI", "JKL"}, "ABC", []int{0, 3, 6, 9}},
	{[]string{"ABC", "DEF", "GHI", "JKL"}, "JKL", []int{17, 20, 23, 0}},
	{[]string{"ABD", "DEG", "GII", "JIL"}, "ABC", []int{}},
	{[]string{"ABC", "DEG", "GII", "JIL"}, "ABC", []int{0}},
}

func TestAllowedShits(t *testing.T) {
	for _, tt := range getAllowedShiftsTests {
		t.Run("", func(t *testing.T) {
			expected := tt.allowedShifts
			actual := getAllowedShifts(tt.dictionary, tt.cipherText)

			if !reflect.DeepEqual(expected, actual) {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

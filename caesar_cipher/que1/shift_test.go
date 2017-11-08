package main

import (
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

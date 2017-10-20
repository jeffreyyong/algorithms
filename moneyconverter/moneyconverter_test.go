package moneyconverter

import (
	"reflect"
	"strconv"
	"testing"
)

var parseWordsTests = []struct {
	word   string
	number int
}{
	{"zero dollars", 0},
	{"one dollar", 1},
	{"three dollars", 3},
	{"twenty dollars", 20},
	{"thirty five dollars", 35},
	{"five hundred and fifty five dollars", 555},
	{"three thousand dollars", 3000},
	{"three thousand two hundred dollars", 3200},
	{"three thousand two hundred and three dollars", 3203},
	{"one trillion two hundred and thirty four billion five hundred and sixty seven million eight hundred and ninety thousand one hundred and twenty three dollars", 1234567890123},
}

var splitDigitsTests = []struct {
	number      int
	numberGroup []int
}{
	{1, []int{1}},
	{1234, []int{1, 234}},
	{123456789, []int{123, 456, 789}},
}

func TestParseWords(t *testing.T) {
	for _, tt := range parseWordsTests {
		t.Run(tt.word, func(t *testing.T) {
			expected := tt.number
			actual, err := ParseWords(tt.word)
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			if expected != actual {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

func TestToWords(t *testing.T) {
	for _, tt := range parseWordsTests {
		t.Run(strconv.Itoa(tt.number), func(t *testing.T) {
			expected := tt.word
			actual := ToWords(tt.number)

			if expected != actual {
				t.Fatalf("expected = %v actual = %v", expected, actual)
			}
		})
	}
}

func TestSplitDigits(t *testing.T) {
	for _, tt := range splitDigitsTests {
		t.Run(strconv.Itoa(tt.number), func(t *testing.T) {
			expected := tt.numberGroup
			actual := splitDigits(tt.number)

			if !reflect.DeepEqual(expected, actual) {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

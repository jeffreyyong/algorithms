package easy

import "testing"

var longestCommonPrefixTests = []struct {
	description string
	strings     []string
	expected    string
}{
	{
		description: "longest common prefix",
		strings:     []string{"abcdd", "abcde", "ab"},
		expected:    "ab",
	},
	{
		description: "longest common prefix 2",
		strings:     []string{"abcdd", "abcde"},
		expected:    "abcd",
	},
	{
		description: "empty string array should return empty string",
		strings:     []string{},
		expected:    "",
	},
}

func TestLongestCommonPrefix(t *testing.T) {
	for _, test := range longestCommonPrefixTests {
		t.Run(test.description, func(t *testing.T) {
			actual := longestCommonPrefix(test.strings)
			if actual != test.expected {
				t.Errorf("Expected %v, but got %v", test.expected, actual)
			}
		})
	}
}

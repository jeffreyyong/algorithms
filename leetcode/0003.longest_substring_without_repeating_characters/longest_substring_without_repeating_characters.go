package problem0003

func lengthOfLongestSubstring(s string) int {

	location := [256]int{}

	// location[s[i]] == j means:
	// The ith string in s, last appeared in the j position of s, so there is no s[i] in s[j + 1:i]
	// Location[s[i]] == -1 means: s[i] first appears in s
	for i := range location {
		location[i] = -1 // Set all the characters to have not seen before
	}

	maxLen, left := 0, 0

	for i := 0; i < len(s); i++ {
		// s[i] has been repeated in s[left: i + 1]
		// And s[i] last appeared in location[s[i]]
		if location[s[i]] >= left {
			left = location[s[i]] + 1 // Remove the s[i] chracter and its preceding part in s[left: i + 1]
		} else if i+1-left > maxLen {
			maxLen = i + 1 - left
		}
		location[s[i]] = i
	}

	return maxLen
}

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Question
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Thought process
Use s[left : i + 1] to represent the longest substring containing s[i] in s[:i + 1]. Location[[s[i]] is the sequence number of the second occurrence
of the character s[i] in s[:i + 1]. When left < location[s[i]], the character s[i] appears twice. Need to set left = location[s[i]] + 1,
This guarantees character s[i] only appears once. 


## Conclusion 
Use Location to save the last occurrence of the character sequence number, to avoid the query work. Location is the same as m in [Two Sum](./algorithms/0001.two_sum)


```go
// m is responsible for saving the sequence number of the map integer
	m := make(map[int]int, len(nums))
```


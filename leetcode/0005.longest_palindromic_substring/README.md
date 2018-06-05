# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## 题目
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
Example:
```
Input: "cbbd"
Output: "bb"
```
## Thought Process 
The question asks for the longest palindrome in the string. 
Can use the following programme to determine if the string s[j:j + 1] is a palindrome. 
```go
func isPalindromic(s *string, i, j int ) bool {
    for  i< j {
        if (*s)[i] != (*s)[j] {
            return false
        } 
        i++
        j--
    }
    return true
}
```
But, this does not take advantage of the palindrome, assuming that the length of the palindrome is l, x is any character
1. When l is odd, the middle segment of the palindrome will ony be "x" or "xxx" or "xxxxx" or ...
2. When l is an even number, the middle segment of the palindrome will only be "xx", "xxxx", "xxxxxx" or ...
3. The middle segment of any two palindrome substrings of the same string will not overlap.

## Conclusion
Making use of these characteristics can speed up the search.


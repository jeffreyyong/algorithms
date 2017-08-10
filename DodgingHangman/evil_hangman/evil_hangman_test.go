package main

import "testing"

func listContains(words []string, word string) bool {
	for _, toMatch := range words {
		if toMatch == word {
			return true
		}
	}
	return false
}

func TestFilterByLen(t *testing.T) {
	words := []string{"a", "b", "c", "bb", "cc", "ccc", "dddd"}
	len1Words := filterByLen(words, 1)
	len2Words := filterByLen(words, 2)

	for _, w := range []string{"a", "b", "c"} {
		if !listContains(len1Words, w) {
			t.Errorf("%s not found on list of length 1", w)
		}
	}

	for _, w := range []string{"bb", "cc"} {
		if !listContains(len2Words, w) {
			t.Errorf("%s not found on list of length 2", w)
		}
	}
}

func TestCommonCharacter(t *testing.T) {
	{
		words := []string{"aacvya", "aafdoa", "aapqsa", "aazxza"}
		commonChars := commonCharacter(words)
		if commonChars != "aa___a" {
			t.Errorf("Common characters do not match")
		}
	}
	{
		words := []string{"bacvya", "aafdoa", "aapqsa", "aazxza"}
		commonChars := commmonCharacter(words)
		if commonChars != "_a___a" {
			t.Errorf("Common characters do not match")
		}
	}
	{
		words := []string{"sdrfww", "aafdoa", "aapqsa", "aazxza"}
		commonChars := commonCharacter(words)
		if commonChars != "______" {
			t.Errorf("Common characters do not match")
		}
	}
}

func TestMaxPartition(t *testing.T) {
	{
		words := []string{"aaa", "aab", "bbd", "bbb", "dcb", "eab"}
		exists, maxPartition := getMaxPartition("b", words)

		if !exists {
			t.Errorf("b should exist in max partition")
		}

		for _, w := range []string{"dcb", "aab", "eab"} {
			if !listContains(maxPartition, w) {
				t.Errorf("max partition is wrong, %s not in max partition", w)
			}
		}

		for _, w := range []string{"aaa", "bbd", "bbb"} {
			if listContains(maxPartition, w) {
				t.Errorf("max partition is wrong, %s in max partition", w)
			}
		}
	}

	{
		words := []string{"aaa", "aab", "bbd", "bbb", "dcb", "eab"}
		exists, maxPartition := getMaxPartition("a", words)
		if exists {
			t.Errorf("a should not exist in max partition")
		}

		for _, w := range []string{"bbd", "bbb", "dcb"} {
			if !listContains(maxPartition, w) {
				t.Error("max partition is wrong")
			}
		}

		for _, w := range []string{"aaa", "aab", "eab"} {
			if listContains(maxPartition, w) {
				t.Errorf("max partition is wrong")
			}
		}
	}

}

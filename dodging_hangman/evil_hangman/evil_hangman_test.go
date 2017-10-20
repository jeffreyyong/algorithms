package main

import (
	"testing"
)

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
		words := []string{"aa1rra", "aa43sa", "aaty2a", "aa431a"}
		commonChars := commonCharacter(words, "______", 'a')
		if commonChars != "aa___a" {
			t.Errorf("Common characters not matches")
		}
	}
	{
		words := []string{"ba1rra", "aa43sa", "aaty2a", "aa431a"}
		commonChars := commonCharacter(words, "_a___a", 'a')
		if commonChars != "_a___a" {
			t.Errorf("Common characters not matches")
		}
	}
	words := []string{"sdfrwe", "aa43sa", "aaty2a", "aa431a"}
	commonChars := commonCharacter(words, "______", 'a')
	if commonChars != "______" {
		t.Errorf("Common characters not matches")
	}
}

func TestMaxPartition(t *testing.T) {

	{
		words := []string{"aaa", "aab", "bbd", "bbb", "dcb", "eab"}
		exists, maxPartition := getMaxPartition('b', words)

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
		exists, maxPartition := getMaxPartition('a', words)
		if exists {
			t.Errorf("a should not exist in max partition")
		}
		for _, w := range []string{"bbd", "bbb", "dcb"} {
			if !listContains(maxPartition, w) {
				t.Errorf("max partition is wrong")
			}
		}

		for _, w := range []string{"aaa", "aab", "eab"} {
			if listContains(maxPartition, w) {
				t.Errorf("max partition is wrong")
			}
		}
	}

	{
		words := []string{"aaa", "aab", "bbd", "bbb", "dcb"}
		exists, maxPartition := getMaxPartition('e', words)
		if exists {
			t.Errorf("e should not exists")
		}
		for _, w := range words {
			if !listContains(maxPartition, w) {
				t.Errorf("max partition is wrong")
			}
		}
	}
}

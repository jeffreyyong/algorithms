package counting_elements

import (
	"testing"
)

func TestMissingInteger(t *testing.T) {
	ans := findMissingInteger([]int{1, 3, 6, 4, 1, 2})
	if ans != 5 {
		t.Errorf("Error, got %d", ans)
	}

	ans = findMissingInteger([]int{1, 2, 3})
	if ans != 4 {
		t.Errorf("Error, got %d", ans)
	}

	ans = findMissingInteger([]int{-1, -3})
	if ans != 1 {
		t.Errorf("Error, got %d", ans)
	}
}

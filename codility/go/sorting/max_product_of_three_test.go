package sorting

import (
	"testing"
)

func TestMaxProductOfThree(t *testing.T) {
	ans := maxProductOfThree([]int{-3, 1, 2, -2, 5, 6})
	if ans != 60 {
		t.Errorf("Error, got %v", ans)
	}
}

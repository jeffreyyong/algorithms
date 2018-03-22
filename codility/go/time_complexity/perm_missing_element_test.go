package time_complexity

import (
	"testing"
)

func TestPermMissingElement(t *testing.T) {
	ans := findMissingElement([]int{2, 3, 1, 5})
	if ans != 4 {
		t.Errorf("Error, got %d", ans)
	}
}

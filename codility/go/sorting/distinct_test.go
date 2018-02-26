package sorting

import (
	"testing"
)

func TestDistinct(t *testing.T) {
	ans := distinct([]int{2, 1, 1, 2, 3, 1})
	if ans != 3 {
		t.Errorf("Error, got %v", ans)
	}
}

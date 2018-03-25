package prefix_sums

import (
	"testing"
)

func TestFindMinAvg(t *testing.T) {
	ans := findMinAvg([]int{4, 2, 2, 5, 1, 5, 8})
	if ans != 1 {
		t.Errorf("Error, got %d", ans)
	}

	ans = findMinAvg([]int{4, 2, 2, 5, -100, 6, 8})
	if ans != 3 {
		t.Errorf("Error, got %d", ans)
	}
}

package counting_elements

import (
	"testing"
)

func TestPermCheck(t *testing.T) {
	ans := permCheck([]int{4, 1, 3, 2})
	if ans != 1 {
		t.Errorf("Error, got %d", ans)
	}

	ans = permCheck([]int{4, 1, 3})
	if ans != 0 {
		t.Errorf("Error, got %d", ans)
	}
}

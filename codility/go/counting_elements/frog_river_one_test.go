package counting_elements

import (
	"testing"
)

func TestFrogRiver(t *testing.T) {
	ans := frogRiver(5, []int{1, 3, 1, 4, 2, 3, 5, 4})
	if ans != 6 {
		t.Errorf("Error, got %d", ans)
	}
}

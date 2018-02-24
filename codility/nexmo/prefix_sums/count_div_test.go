package prefix_sums

import (
	"testing"
)

func TestCountDiv(t *testing.T) {
	ans := countDiv(6, 11, 2)
	if ans != 3 {
		t.Errorf("Error, got %d", ans)
	}
}

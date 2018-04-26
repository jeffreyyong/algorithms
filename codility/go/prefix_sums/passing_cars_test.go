package prefix_sums

import (
	"testing"
)

func TestCountPassingCars(t *testing.T) {
	ans := countPassingCars([]int{0, 1, 0, 1, 1})
	if ans != 5 {
		t.Errorf("Error, got %d", ans)
	}
}

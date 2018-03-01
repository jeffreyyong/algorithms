package time_complexity

import (
	"testing"
)

func TestFrogJump(t *testing.T) {
	ans := frogJump(10, 85, 30)
	if ans != 3 {
		t.Errorf("Error, got %d", ans)
	}
}

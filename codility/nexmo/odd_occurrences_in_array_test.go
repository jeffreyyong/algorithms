package nexmo

import (
	"testing"
)

func TestOddOccurrence(t *testing.T) {
	ans := findOdd([]int{9, 3, 9, 3, 9, 7, 9})
	if ans != 7 {
		t.Errorf("Error, got %d", ans)
	}
}

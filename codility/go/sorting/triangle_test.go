package sorting

import (
	"testing"
)

func TestTriangle(t *testing.T) {
	ans := triangle([]int{10, 2, 5, 1, 8, 20})
	if ans != 1 {
		t.Errorf("Error, got %v", ans)
	}

	ans = triangle([]int{10, 50, 5, 1})
	if ans != 0 {
		t.Errorf("Error, got %v", ans)
	}
}

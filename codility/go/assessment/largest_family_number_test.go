package assessment

import (
	"testing"
)

func TestLargestFamilyNumber(t *testing.T) {
	ans := Solution(213)
	if ans != 321 {
		t.Errorf("Error, got %v", ans)
	}

	ans = Solution(553)
	if ans != 553 {
		t.Errorf("Error, got %v", ans)
	}
}

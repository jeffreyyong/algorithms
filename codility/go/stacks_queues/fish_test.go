package stacks_queues

import (
	"testing"
)

func TestFish(t *testing.T) {
	ans := fishAlive([]int{4, 3, 2, 1, 5}, []int{0, 1, 0, 0, 0})
	if ans != 2 {
		t.Errorf("Error, got %v", ans)
	}
}

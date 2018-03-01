package stacks_queues

import (
	"testing"
)

func TestNesting(t *testing.T) {
	ans := nesting("(()(())())")
	if ans != 1 {
		t.Errorf("Error, got %v", ans)
	}

	ans = nesting("())")
	if ans != 0 {
		t.Errorf("Error, got %v", ans)
	}
}

package stacks_queues

import (
	"testing"
)

func TestBrackets(t *testing.T) {
	ans := brackets("{[()()]}")
	if ans != 1 {
		t.Errorf("Error, got %v", ans)
	}

	ans = brackets("{[(]}")
	if ans != 0 {
		t.Errorf("Error, got %v", ans)
	}
}

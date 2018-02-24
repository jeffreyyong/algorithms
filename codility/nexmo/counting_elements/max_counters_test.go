package counting_elements

import (
	"reflect"
	"testing"
)

func TestMaxCounters(t *testing.T) {
	ans := findMaxCounters(5, []int{3, 4, 4, 6, 1, 4, 4})
	if !reflect.DeepEqual(ans, []int{3, 2, 2, 4, 2}) {
		t.Errorf("Error, got %d", ans)
	}
}

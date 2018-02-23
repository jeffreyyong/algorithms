package nexmo

import (
	"reflect"
	"testing"
)

func TestCyclicRotation(t *testing.T) {
	ans := cyclicRotation([]int{3, 8, 9, 7, 6}, 3)
	if !reflect.DeepEqual(ans, []int{9, 7, 6, 3, 8}) {
		t.Errorf("Error, got %d", ans)
	}
}

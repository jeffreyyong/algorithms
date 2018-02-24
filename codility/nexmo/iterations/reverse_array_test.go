package iterations

import (
	"reflect"
	"testing"
)

func TestSum(t *testing.T) {
	total := Sum(5, 5)
	if total != 10 {
		t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 10)
	}
}

func TestReverseArray(t *testing.T) {
	reversedArray := reverse([]int{1, 2, 3, 4, 5})
	if !reflect.DeepEqual(reversedArray, []int{5, 4, 3, 2, 1}) {
		t.Errorf("Failed!, got: %+v", reversedArray)
	}
}

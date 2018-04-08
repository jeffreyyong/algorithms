package prefix_sums

import (
	"reflect"
	"testing"
)

func TestGenomicQueryRange(t *testing.T) {
	ans := genomicRangeQuery("CAGCCTA", []int{2, 5, 0}, []int{4, 5, 6})
	if !reflect.DeepEqual(ans, []int{2, 4, 1}) {
		t.Errorf("Error, got %v", ans)
	}
}

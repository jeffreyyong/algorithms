package main

import (
	"fmt"
	"testing"
)

var containOriginTests = []struct {
	points []Point
	result bool
}{
	{[]Point{Point{2, 3}, Point{3, 2}, Point{-1, -1}}, true},
	{[]Point{Point{2, 3}, Point{4, 1}, Point{-1, -1}}, true},
	{[]Point{Point{2, 3}, Point{4, 1}, Point{3, 2}}, false},
}

func TestCheckingPointsContainOrigin(t *testing.T) {
	for _, tt := range containOriginTests {
		pointsString := fmt.Sprintf("%#v", tt.points)
		t.Run(pointsString, func(t *testing.T) {
			expected := tt.result
			actual := checkTriangle(tt.points[0], tt.points[1], tt.points[2])
			// actual, err := ParseWords(tt.word)

			if expected != actual {
				t.Fatalf("expected=%v actual=%v", expected, actual)
			}
		})
	}
}

// func TestCheckingPointsContainOrigin(t *testing.T) {
// 	for _, tt = range containOriginTests {
// 		t.Run(tt.points, funct(t *testing.T) {
// 			expected := tt.result
// 			points = tt.points
// 			actual := checkTriangle(points[0], points[1], points[2])

// 			if expected != actual {
// 				t.Fatalf("expected=%v actual=%v", expected, actual)
// 			}
// 		})
// 	}
// }

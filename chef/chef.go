package main

import (
	"fmt"
	// "strconv"
)

/// Points struct..we have created an array of this struct named arr..which is dynamic
type Point struct {
	x int
	y int
}

const numberOfPoints = 3

var (
	count          int
	containsOrigin bool
)

func main() {
	var number int

	number = 6

	p1 := Point{2, 3}
	p2 := Point{3, 2}
	p3 := Point{-1, -1}
	p4 := Point{3, 3}
	p5 := Point{4, 1}
	p6 := Point{5, 5}

	allPoints := []Point{p1, p2, p3, p4, p5, p6}

	// number = 10

	// p1 := Point{1, 3}
	// p2 := Point{2, 10}
	// p3 := Point{1, -5}
	// p4 := Point{1, 6}
	// p5 := Point{2, 3}
	// p6 := Point{3, 0}
	// p7 := Point{-2, -1}
	// p8 := Point{3, 4}
	// p9 := Point{4, 1}
	// p10 := Point{5, 5}

	// allPoints := []Point{p1, p2, p3, p4, p5, p6, p7, p8, p9, p10}

	pointArray := make([]Point, 0)

	for i := 0; i < number; i++ {

		pointArray = append(pointArray, allPoints[i])

		if num := i; num < 2 {
			fmt.Println(0)
		} else {
			checkCount(pointArray, i+1)
			///print the count as output if origins are in points set
			fmt.Println(count)
			/// resetting the count for next iteration
			count = 0
		}
	}
}

func checkOrigin(a Point, b Point) float32 {
	var val int
	val = (0-b.x)*(a.y-b.y) - (a.x-b.x)*(0-b.y)
	return float32(val)
}

func checkTriangle(a Point, b Point, c Point) bool {
	var b1 bool
	var b2 bool
	var b3 bool

	var val1 float32
	var val2 float32
	var val3 float32

	val1 = checkOrigin(a, b)
	val2 = checkOrigin(b, c)
	val3 = checkOrigin(c, a)

	/// if any val is zero that means origin is not in the set
	if val1 == 0.0 || val2 == 0.0 || val3 == 0.0 {
		return false
	}

	if val1 < 0.0 {
		b1 = true
	}
	if val2 < 0.0 {
		b2 = true
	}
	if val3 < 0.0 {
		b3 = true
	}

	if (b1 == b2) && (b2 == b3) {
	}
	return ((b1 == b2) && (b2 == b3))
}

/// getting combination subsets of 3 points of that array
func subset(pointArray []Point, number int, index int, res [3]Point, i int) {

	if index == numberOfPoints {
		// fmt.Println(res)
		containsOrigin = checkTriangle(res[0], res[1], res[2])
		if containsOrigin {
			count++
		}
		return
	}

	if i >= number {
		return
	}
	// adding 3 points data to each res
	res[index] = pointArray[i]
	subset(pointArray, number, index+1, res, i+1)
	// fmt.Println("first recurisve index: ", strconv.Itoa(index))
	subset(pointArray, number, index, res, i+1)
	// fmt.Println("second recurisve index: ", strconv.Itoa(index))
}

func checkCount(arr []Point, number int) {
	var res [3]Point
	subset(arr, number, 0, res, 0)
}

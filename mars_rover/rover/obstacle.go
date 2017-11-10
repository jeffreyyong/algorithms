package rover

import "fmt"

type obstacle struct {
	Point point
}

func (o *obstacle) Set(X, Y int) *obstacle {
	o.Point = point{X, Y}
	return o
}

func (o *obstacle) CheckAndAvoidance(r Rover) *Rover {
	end := r.final
	start := r.initial
	s := (end.Point.Y-o.Point.Y)*start.Point.X + (o.Point.X-end.Point.X)*start.Point.Y + (end.Point.X*o.Point.Y - o.Point.X*end.Point.Y)

	if start.Point != o.Point {
		if s == 0 {
			fmt.Printf("obstacle at position %v \n", o)
			r.Path = r.initialPath
		}
	}
	return &r
}

package rover

import (
	"math"
)

type position struct {
	Point  point
	Degree int16
}

func (p *position) Rotate(degree int16) *position {
	if degree < 0 {
		degree = 360 + degree
	}
	p.Degree = (degree + p.Degree) % 360
	return p // keep it chainable
}

// update positions point with new x and y
// consider positions degree when moving
func (p *position) MoveInDirection(ticks int) *position {
	// do cos(n°) and convert n° to rad before
	p.Point.X = p.Point.X + ticks*int(math.Cos(float64(p.Degree)*math.Pi/180.0))

	// do sin(n°) and convert n° to rad before
	p.Point.Y = p.Point.Y + ticks*int(math.Sin(float64(p.Degree)*math.Pi/180.0))

	return p // keep it chainable
}

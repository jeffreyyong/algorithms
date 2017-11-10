package rover

//import "fmt"

type Map struct {
	height    int
	width     int
	obstacles []obstacle
	rovers    []Rover
}

func (m *Map) SetDimensions(h, w int) *Map {
	m.height = h
	m.width = w
	return m
}

/*func (m *Map) CheckForObstacles() {
	for _, rover := range m.rovers {
		for _, obstacle := range m.obstacles {
			rover = *obstacle.CheckAndAvoidance(rover)
		}
	}
}*/

func (m *Map) Wrap(rover *Rover) *Rover {
	bx := m.width / 2
	by := m.height / 2
	position := rover.Path[len(rover.Path)-1]
	if position.Point.Y < 0 {
		position.Point.Y = by + position.Point.Y%by
	} else if position.Point.Y < by {

	} else {
		position.Point.Y = -by + position.Point.Y%by
	}
	if position.Point.X < 0 {
		position.Point.X = bx + position.Point.X%bx
	} else if position.Point.X < bx {

	} else {
		position.Point.X = -bx + position.Point.X%bx
	}
	rover.SetWrap(position)
	return rover
}

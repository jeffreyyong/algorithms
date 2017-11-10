package rover

import (
	"fmt"
	"strings"
)

type Rover struct {
	Path        []position
	initial     position
	final       position
	initialPath []position
}

func (r *Rover) Init(x, y int, degree int16) *Rover {
	r.Path = append(r.Path, position{point{x, y}, degree})
	return r
}

func (r *Rover) CurrentPosition() *position {
	if len(r.Path) > 0 {
		return &r.Path[len(r.Path)-1]
	}
	return nil
}

func (r *Rover) SetWrap(position position) *Rover {
	r.Path[len(r.Path)-1] = position
	return r
}

func (r *Rover) Command(command string) *Rover {
	commandSlice := strings.Split(command, "")
	r.initial = *r.CurrentPosition()
	r.initialPath = r.Path
	for _, value := range commandSlice {
		switch value {
		case "f":
			r.Move(1) // move 1 tick forward
		case "b":
			r.Move(-1) // move 1 tick backward
		case "l":
			r.Turn(-90) // turn left (rotate by 90d)
		case "r":
			r.Turn(90) // turn right (rotate by 90d)
		}
	}
	r.final = *r.CurrentPosition()
	return r
}

func (r *Rover) Move(ticks int) *Rover {
	d := *r.CurrentPosition()
	//d.MoveInDirection(ticks)
	if ticks == 1 {
		switch d.Degree {
		case 0:
			d.Point.Y = d.Point.Y + 1
		case 90:
			d.Point.X = d.Point.X + 1
		case 180:
			d.Point.Y = d.Point.Y - 1
		case 270:
			d.Point.X = d.Point.X - 1
		}
	} else {
		switch d.Degree {
		case 0:
			d.Point.Y = d.Point.Y - 1
		case 90:
			d.Point.X = d.Point.X - 1
		case 180:
			d.Point.Y = d.Point.Y + 1
		case 270:
			d.Point.X = d.Point.X + 1
		}
	}
	r.Path = append(r.Path, d)
	return r
}

func (r *Rover) Turn(degree int16) *Rover {
	d := *r.CurrentPosition()
	d.Rotate(degree)
	r.Path = append(r.Path, d)
	return r
}

// convenience toString method
func (r Rover) String() string {
	p := r.CurrentPosition()
	/*if p.Degree < 0 {
		p.Degree = 360 + p.Degree
	}*/
	degreeString := ""
	switch p.Degree {
	case 0:
		degreeString = "NORTH"
	case 90:
		degreeString = "EAST"
	case 180:
		degreeString = "SOUTH"
	case 270:
		degreeString = "WEST"
	}
	return fmt.Sprintf("(x%v|y%v), %v° = %v", p.Point.X, p.Point.Y, p.Degree, degreeString)
}

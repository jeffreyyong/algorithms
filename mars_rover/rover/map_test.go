package rover

import (
	"testing"
)

func TestRover_Command(t *testing.T) {
	m := Map{}
	m.SetDimensions(8, 8)

	ob := obstacle{point{2, 2}}
	ob1 := obstacle{point{2, 4}}
	m.obstacles = append(m.obstacles, ob, ob1)

	r1 := Rover{}
	r1.Init(0, 0, 0)
	r2 := Rover{}
	r2.Init(4, 4, 90)
	m.rovers = append(m.rovers, r1, r2)

	r1.Command("ffrff")
	if r1.CurrentPosition().Point.X != 2 || r1.CurrentPosition().Point.Y != 2 || r1.CurrentPosition().Degree != 90 {
		t.Errorf("expected (x2|y2), 90°, got %v", r1)
	}
	r2.Command("ffrff")
	if r2.CurrentPosition().Point.X != 6 || r2.CurrentPosition().Point.Y != 2 || r2.CurrentPosition().Degree != 180 {
		t.Errorf("expected (x2|y2), 90°, got %v", r2)
	}
}

func TestMap_Wrap(t *testing.T) {
	m := Map{}
	m.SetDimensions(8, 8)

	r2 := Rover{}
	r2.Init(4, 4, 90)
	m.rovers = append(m.rovers, r2)

	r2.Command("ffrff")
	r2 = *m.Wrap(&r2)
	if r2.CurrentPosition().Point.X != -2 || r2.CurrentPosition().Point.Y != 2 || r2.CurrentPosition().Degree != 180 {
		t.Errorf("expected (x-2|y2), 90°, got %v", r2)
	}
}

func TestMap_CheckForObstacles(t *testing.T) {
	m := Map{}
	m.SetDimensions(8, 8)

	ob := obstacle{point{2, 2}}
	ob1 := obstacle{point{6, 3}}
	m.obstacles = append(m.obstacles, ob, ob1)

	r1 := Rover{}
	r1.Init(0, 0, 0)
	r2 := Rover{}
	r2.Init(4, 4, 90)
	m.rovers = append(m.rovers, r1, r2)

	r1.Command("ffrff")
	r2.Command("ffrff")
	for _, obstacle := range m.obstacles {
		r1 = *obstacle.CheckAndAvoidance(r1)
	}
	if r1.CurrentPosition().Point.X != 0 || r1.CurrentPosition().Point.Y != 0 || r1.CurrentPosition().Degree != 0 {
		t.Errorf("expected (x0|y0), 0°, got %v", r1)
	}
	for _, obstacle := range m.obstacles {
		r2 = *obstacle.CheckAndAvoidance(r2)
	}
	if r2.CurrentPosition().Point.X != 6 || r2.CurrentPosition().Point.Y != 2 || r2.CurrentPosition().Degree != 180 {
		t.Errorf("expected (x2|y2), 90°, got %v", r2)
	}
}

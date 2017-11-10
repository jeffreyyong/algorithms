package rover

import "testing"

func TestExistingObstacle(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)
	ob := obstacle{}
	ob.Set(1, 1)

	r.Command("ffrff")
	r = *ob.CheckAndAvoidance(r)
	if r.CurrentPosition().Point.X != 0 || r.CurrentPosition().Point.Y != 0 || r.CurrentPosition().Degree != 0 {
		t.Errorf("expected (x0|y0), 0°, got %v", r)
	}
}

func TestNonObstacle(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)
	ob := obstacle{}
	ob.Set(5, 1)

	r.Command("ffrff")
	r = *ob.CheckAndAvoidance(r)
	if r.CurrentPosition().Point.X != 2 || r.CurrentPosition().Point.Y != 2 || r.CurrentPosition().Degree != 90 {
		t.Errorf("expected (x0|y0), 0°, got %v", r)
	}
}

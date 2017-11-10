package rover

import (
	"testing"
)

func TestForwardRightCommand(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)

	r.Command("ffrff")
	if r.CurrentPosition().Point.X != 2 || r.CurrentPosition().Point.Y != 2 || r.CurrentPosition().Degree != 90 {
		t.Errorf("expected (x2|y2), 90°, got %v", r)
	}
}

func TestForwardLeftCommand(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)

	r.Command("fflff")
	if r.CurrentPosition().Point.X != -2 || r.CurrentPosition().Point.Y != 2 || r.CurrentPosition().Degree != 270 {
		t.Errorf("expected (x2|y2), 270°, got %v", r)
	}
}

func TestBackwardRightCommand(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)

	r.Command("bblbb")
	if r.CurrentPosition().Point.X != 2 || r.CurrentPosition().Point.Y != -2 || r.CurrentPosition().Degree != 270 {
		t.Errorf("expected (x2|y-2), 270°, got %v", r)
	}
}

func TestBackwardLeftCommand(t *testing.T) {
	r := Rover{}
	r.Init(0, 0, 0)

	r.Command("bbrbb")
	if r.CurrentPosition().Point.X != -2 || r.CurrentPosition().Point.Y != -2 || r.CurrentPosition().Degree != 90 {
		t.Errorf("expected (x-2|y-2), 90°, got %v", r)
	}
}

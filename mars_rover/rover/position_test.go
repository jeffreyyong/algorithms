package rover

import (
	"testing"
)

func TestMoveInDirection(t *testing.T) {
	d := position{}

	d = position{point{0, 0}, 0}
	if d2 := d.MoveInDirection(1); d2.Point.X != 1 || d2.Point.Y != 0 {
		t.Errorf("expected 1,0, got %v", d2)
	}

	d = position{point{0, 0}, 90}
	if d2 := d.MoveInDirection(1); d2.Point.X != 0 || d2.Point.Y != 1 {
		t.Errorf("expected 0,1, got %v", d2)
	}

	d = position{point{0, 0}, 180}
	if d2 := d.MoveInDirection(1); d2.Point.X != -1 || d2.Point.Y != 0 {
		t.Errorf("expected -1,0, got %v", d2)
	}

	d = position{point{0, 0}, 270}
	if d2 := d.MoveInDirection(1); d2.Point.X != 0 || d2.Point.Y != -1 {
		t.Errorf("expected 0,-1, got %v", d2)
	}

	d = position{point{0, 0}, 0}
	if d2 := d.MoveInDirection(-1); d2.Point.X != -1 || d2.Point.Y != 0 {
		t.Errorf("expected -1,0, got %v", d2)
	}

	d = position{point{0, 0}, 90}
	if d2 := d.MoveInDirection(-1); d2.Point.X != 0 || d2.Point.Y != -1 {
		t.Errorf("expected 0,-1, got %v", d2)
	}

	d = position{point{0, 0}, 180}
	if d2 := d.MoveInDirection(-1); d2.Point.X != 1 || d2.Point.Y != 0 {
		t.Errorf("expected 1,0, got %v", d2)
	}

	d = position{point{0, 0}, 270}
	if d2 := d.MoveInDirection(-1); d2.Point.X != 0 || d2.Point.Y != 1 {
		t.Errorf("expected 0,1, got %v", d2)
	}

}

func TestRotate(t *testing.T) {
	d := position{}

	d = position{point{0, 0}, 0}
	if d2 := d.Rotate(90); d2.Degree != 90 {
		t.Errorf("expected 90, got %v", d2.Degree)
	}

	d = position{point{0, 0}, 0}
	if d2 := d.Rotate(-90); d2.Degree != 270 {
		t.Errorf("expected -90, got %v", d2.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(45); d.Degree != 45 {
		t.Errorf("expected 45, got %v", d.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(-45); d.Degree != 315 {
		t.Errorf("expected -45, got %v", d.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(360); d.Degree != 0 {
		t.Errorf("expected 0, got %v", d.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(-360); d.Degree != 0 {
		t.Errorf("expected 0, got %v", d.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(361); d.Degree != 1 {
		t.Errorf("expected 1, got %v", d.Degree)
	}

	d = position{point{0, 0}, 0}
	if d.Rotate(-361); d.Degree != -1 {
		t.Errorf("expected -1, got %v", d.Degree)
	}

	d = position{point{0, 0}, 90}
	if d.Rotate(90); d.Degree != 180 {
		t.Errorf("expected 180 got %v", d.Degree)
	}
}

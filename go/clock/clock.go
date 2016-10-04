package clock

import (
	"fmt"
)

// The value of testVersion here must match `targetTestVersion` in the file
// clock_test.go.
const testVersion = 4

type Clock struct {
	minute int
	hour   int
}

func New(hour, minute int) Clock {

	var clock = new(Clock)

	hourRem := hour % 24
	minRem := minute % 60
	minQuot := minute / 60
	minQuot = minQuot % 24

	if hour >= 0 {
		clock.hour = hourRem
	} else {
		clock.hour = 24 + hourRem
	}

	if minute >= 0 {
		clock.minute = minRem
		clock.hour = clock.hour + minQuot
	} else {
		clock.minute = 60 + minRem
		clock.hour = 24 + clock.hour + minQuot - 1
	}
	clock.hour = clock.hour % 24
	return *clock
}

func (clock Clock) String() string {
	return fmt.Sprintf("%02d:%02d", clock.hour, clock.minute)
}

func (clock Clock) Add(minutes int) Clock {
	return New(clock.hour, clock.minute+minutes)
}

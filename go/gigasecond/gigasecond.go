// Package gigasecond add gigasecond to time.
package gigasecond

import (
	"time"
)

// Constant declaration.
const testVersion = 4

// AddGigasecond add gigasecond to timer
func AddGigasecond(timer time.Time) time.Time {
	return timer.Add(1000000000 * time.Second)
}

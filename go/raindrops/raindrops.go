package raindrops

import (
	"strconv"
)

const testVersion = 2

func Convert(num int) string {
	var text string

	if num%3 == 0 {
		text = text + "Pling"
	}
	if num%5 == 0 {
		text = text + "Plang"
	}
	if num%7 == 0 {
		text = text + "Plong"
	}
	if text == "" {
		text = strconv.Itoa(num)
	}
	return text
}

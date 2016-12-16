package triangle

import (
	"math"
)

const testVersion = 3

type Kind string

var NaT = Kind("NaT") // not a triangle
var Equ = Kind("Equ") // equilateral
var Iso = Kind("Iso") // isosceles
var Sca = Kind("Sca") // scalene

// Code this function.
func KindFromSides(a, b, c float64) Kind {

	if math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) || math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) {
		return NaT
	}
	if a <= 0 || b <= 0 || c <= 0 {
		return NaT
	}
	if a+b < c || a+c < b || b+c < a {
		return NaT
	}
	if a == b && b == c && c == a {
		return Equ
	}
	if a == b || b == c || c == a {
		return Iso
	}
	return Sca

}

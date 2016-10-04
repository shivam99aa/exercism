package hamming

import (
	"errors"
)

const testVersion = 5

// Distance function to calculate hamming distance
func Distance(a, b string) (int, error) {
	var hamming = 0

	if len(a) == len(b) {
		for index, _ := range a {
			if b[index] != a[index] {
				hamming++
			}
		}
	} else {
		return -1, errors.New("Unequal strands")
	}

	return hamming, nil
}

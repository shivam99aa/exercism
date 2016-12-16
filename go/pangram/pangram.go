package pangram

import (
	"strings"
)

const testVersion = 1

func IsPangram(sentence string) bool {
	verify := make(map[int]bool)
	for i := 97; i <= 122; i++ {
		verify[i] = false
	}

	sentence = strings.ToLower(sentence)
	stringByte := []byte(sentence)
	for _, value := range stringByte {
		if (value >= 97 && value <= 122) || value == 32 {
			verify[int(value)] = true
		}
	}

	for _, value := range verify {
		if value == false {
			return false
		}
	}

	return true
}

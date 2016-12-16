package secret

import (
	"strconv"
)

const testVersion = 1

func Handshake(n uint) []string {

	output := make([]string, 0)
	count := int64(n)
	counter := 0
	binaryCount := strconv.FormatInt(count, 2)
	for i := len(binaryCount) - 1; i >= 0; i-- {
		if uint(binaryCount[i]) == 49 {
			switch counter {
			case 0:
				output = append(output, "wink")
			case 1:
				output = append(output, "double blink")
			case 2:
				output = append(output, "close your eyes")
			case 3:
				output = append(output, "jump")
			case 4:
				output = reverse(output)
			}

		}
		counter++
	}
	return output
}

func reverse(numbers []string) []string {
	for i := 0; i < len(numbers)/2; i++ {
		j := len(numbers) - i - 1
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	return numbers
}

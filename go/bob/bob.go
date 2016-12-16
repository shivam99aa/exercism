package bob // package name must match the package name in bob_test.go

import (
	"strings"
)

const testVersion = 2 // same as targetTestVersion

func Hey(message string) string {

	message = strings.TrimSpace(message)

	if message == strings.ToUpper(message) && message != strings.ToLower(message) {
		return "Whoa, chill out!"
	} else if strings.HasSuffix(message, "?") {
		return "Sure."
	} else if len(message) == 0 {
		return "Fine. Be that way!"
	}
	return "Whatever."
}

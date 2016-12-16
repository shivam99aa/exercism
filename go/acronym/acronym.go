package acronym

import (
	"regexp"
	"strings"
	"unicode"
)

const testVersion = 1

func abbreviate(message string) string {

	var acronym = ""
	var regex = regexp.MustCompile(`[^a-zA-Z0-9]`)
	//var caps = regexp.MustCompile(`[A-Z]`)
	splitMessage := regex.Split(message, -1)
	for _, words := range splitMessage {
		words = strings.TrimSpace(words)
		if len(words) == 0 {
			continue
		}
		acronym = acronym + strings.ToUpper(string(words[0]))
		flag := true

		for _, char := range words[1:] {
			if unicode.IsUpper(char) && !flag {
				acronym = acronym + string(char)
				flag = true
			} else if unicode.IsLower(char) {
				flag = false
			}
		}
	}
	return acronym
}

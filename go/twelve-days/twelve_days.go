package twelve

import (
	//"fmt"
	"strings"
)

const testVersion = 1

var start = "On the "
var num = [...]string{"first", "second",
	"third", "fourth",
	"fifth", "sixth",
	"seventh", "eighth",
	"ninth", "tenth",
	"eleventh", "twelfth",
}
var middle = " day of Christmas my true love gave to me, "
var gifts = [...]string{"a Partridge in a Pear Tree",
	"two Turtle Doves",
	"three French Hens",
	"four Calling Birds",
	"five Gold Rings",
	"six Geese-a-Laying",
	"seven Swans-a-Swimming",
	"eight Maids-a-Milking",
	"nine Ladies Dancing",
	"ten Lords-a-Leaping",
	"eleven Pipers Piping",
	"twelve Drummers Drumming",
}

func Verse(index int) string {
	index--
	song := start + num[index] + middle
	for i := index; i >= 0; i-- {
		if index > 0 && i == 0 {
			song = song + "and " + gifts[i] + ", "
		} else {
			song = song + gifts[i] + ", "
		}
	}
	song = strings.TrimSuffix(song, ", ")
	song = song + "."
	return song
}

func Song() string {
	song := ""

	for i := 1; i <= 12; i++ {
		song = song + Verse(i) + "\n"
	}
	return song
}

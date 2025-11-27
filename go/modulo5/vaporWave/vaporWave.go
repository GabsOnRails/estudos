// Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

// Note that spaces should be ignored in this case.

package main

import (
	"strings"
	"unicode"
)

func main() {
}

func Vaporcode(loweString string) string {

	upperCaseLetters := strings.ToUpper(loweString)
	vaporWaveString := ""

	for _, letters := range upperCaseLetters {
		char := string(letters)
		if char != " " {
			vaporWaveString += char + "  "
		}

	}
	removeSpace := strings.TrimRightFunc(vaporWaveString, unicode.IsSpace)
	return removeSpace
}

package main

import (
	"strconv"
)

func main() {
	// number := 5
	// fmt.Sprintf("%d",number) -> transforma qualquer número em string.

}

func NumberToString(n int) string {
	intToString := strconv.Itoa(n)
	return intToString
}

package main

import (
	"fmt"
)

func main() {
	fmt.Print(HighAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
}

func HighAndLow(numbersStr string) string {
	fmt.Printf("type %T", numbersStr)
	x := (numbersStr[0])
	fmt.Println(x)
	return "ah"
}

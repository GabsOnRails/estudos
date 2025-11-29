// Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
// For example: (Input --> Output)
// 10 --> 1
// 99 --> 18
// -32 --> 5
// Let's assume that all numbers in the input will be integer values.

// I need to convert a number to in string and after this, i will use for loop to take individual string
// and convert in number. Finally I will sum the numbers and return the value.

package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(SumDigits(10))
}

func SumDigits(number int) int {
	sumInt := 0
	numberToString := strconv.Itoa(number)
	for _, value := range numberToString {
		char := string(value)
		stringToInt, _ := strconv.Atoi(char)
		sumInt += stringToInt
	}
	// your code here
	return sumInt
}

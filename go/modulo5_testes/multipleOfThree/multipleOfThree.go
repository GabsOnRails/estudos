package main

import (
	"strconv"
)

func main() {

}

func PrevMultOfThree(number int) interface{} {
	if number%3 == 0 {
		return (number)
	} else {
		numberToString := strconv.Itoa(number)
		for len(numberToString) > 1 {
			numberToString = numberToString[:len(numberToString)-1]
			newNumber, _ := strconv.Atoi(numberToString)
			if newNumber%3 == 0 {
				return newNumber
			}
		}

	}
	return nil
}

// !A simple way to do that. Just divide per 10, because this remove the decimal.
// func PrevMultOfThree(n int) interface{} {

//     for i := n; i > 0; i /= 10 {
//         if i % 3 == 0 {
//             return i
//         }
//     }

//     return nil
// }

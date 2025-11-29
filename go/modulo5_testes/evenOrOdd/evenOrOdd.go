// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

package main

func EvenOrOdd(number int) string {
	if number%2 == 0 { //se numero / 2 for 0, ou seja, par, retornar Even.
		return "Even"
	}
	return "Odd"

}

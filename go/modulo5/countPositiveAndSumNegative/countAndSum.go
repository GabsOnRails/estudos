package main

import "fmt"

func main() {

	fmt.Println(CountPositivesSumNegatives([]int{}))

}

func CountPositivesSumNegatives(numbers []int) []int {
	var res []int
	sum := 0
	counter := 0
	for _, number := range numbers {
		if number > 0 {
			counter += 1
		} else {
			sum += number
		}
	}
	res = []int{counter, sum}
	return res
}

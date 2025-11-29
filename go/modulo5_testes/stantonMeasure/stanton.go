package main

import "fmt"

func main() {
	fmt.Println(StantonMeasure([]int{1, 4, 3, 2, 1, 2, 3, 2}))
}

func StantonMeasure(nums []int) int {
	const target = 1                  // n is the number that we used for the first search.
	var countTarget, statonResult int // countTarget is the number of times n appears in the nums.

	for _, number := range nums {
		if number == target {
			countTarget++
		}

	}
	for _, number := range nums {
		if number == countTarget {
			statonResult++
		}
	}

	return statonResult
}

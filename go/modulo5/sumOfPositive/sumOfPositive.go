// sum of positive numbers, if a number is negative the default value is 0.

//Tenho que fazer um for para percorrer os valores e depois uma condicional com if para somar so os positivos.

package main

import "fmt"

func main() {
	fmt.Println(PositiveSum([]int{1, -2, 3, 4, 5}))

}

func PositiveSum(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		if number > 0 {
			sum += number
		} else {
			sum += 0
		}
	}
	return sum

}

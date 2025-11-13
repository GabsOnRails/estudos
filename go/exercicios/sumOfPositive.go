//go:build ignore

package main

import (
	"fmt"
)
func main () {
	fmt.Println(PositiveSum([]int{1, 2, 3, 4, 5}))

}

func PositiveSum(numbers []int) int {
index := len(numbers)-1
numSum := 0
sum := 0
counter := index

for i := 0; i <= index ; i ++ {
	fmt.Println(counter)
	numSum = numbers[counter]
	fmt.Println(numSum)
	if numSum > 0 {
		sum += numSum
	} else {
		numSum = 0
	}
	counter -= 1 

}
return sum


}
 





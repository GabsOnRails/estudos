// Preciso fazer um algoritmo que receba um array de int e, caso tenha algum número positivo que retorne o valor negativo daquele número. 0 irá retornar zero e negativo irá retornar o próprio valor.

package main

// func main() {
// 	testeArray := []int{-2}
// 	fmt.Println(Invert(testeArray))
// }

// fazer arr * (-1)

func Invert(arr []int) []int {
	newArr := []int{}
	for _, elementArr := range arr {
		newArr = append(newArr, -elementArr)
	}
	return newArr
}

// Preciso fazer um algoritmo que recebe um valor e uma string e retorna uma string
// que repete o valor pela quantidade passada. Ex: func repeat(2,"a") -> saída "aa"
// Vou tentar fazer de forma manual. Falhei miseravelmente, mas tem uma func no package main. Dá pra usar for.

package main

import "strings"

func main() {
	// fmt.Println(testeRepeat(4, "ola"))
}

func RepeatStr(repetitions int, value string) string {
	//com func do package main
	return strings.Repeat(value, repetitions)
	// com for
	// stringNova := ""
	// for i := 0; i < repetitions; i++ {
	// 	stringNova += value
	// }
	// return stringNova
}

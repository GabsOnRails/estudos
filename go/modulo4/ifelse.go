//go:build ignore

package main

import (
	"fmt"
)
func main () {
	//if else padrao if (condicao) {acao a ser feita}

	numero := 3
	if numero == 1 {
		fmt.Println("O valor é 1")
	} else {
	fmt.Printf("O valor %d diferente de 1: \n",numero)
	}

	// Esse caso é interessante, dá para usar o else if para colocar mais uma condição.
	if numero == 1 {
		fmt.Println("Número igual a 1.")
	} else if numero == 2{
		fmt.Println("Número igual a 2.")
	} else {
		fmt.Println("O número não é 1 e nem 2.")
	} 

	if numero%2 == 0 {
		fmt.Printf("O número %d é par.\n",numero)
	} else {
		fmt.Printf("O número %d é impar.\n",numero)
	}
}

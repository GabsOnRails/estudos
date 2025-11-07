//go:build ignore

// Tipos:
// bool -> True or false
// string -> Sequencia de bytes
// int -> numeros inteiros
// float (float64 e float32) -> numeros decimais

package main

import (
	"fmt"
)

func main () {
	//printando os tipos de variaveis.
	fmt.Printf("Type: %T - Value: %v\n",true,false)
	fmt.Printf("Type: %T - Value: %v\n",1,1)
	fmt.Printf("Type: %T - Value: %v\n","1","1")
	fmt.Printf("Type: %T - Value: %v\n",1.234,1.234)
}


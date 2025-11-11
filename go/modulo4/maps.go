//go:build ignore

package main

import (
	"fmt"
)
func main () {

//Definindo map vazio e incrementando chave-valor.
idade := map [string] int {}
idade["gabriel"] = 25

fmt.Println(idade["gabriel"])

//Declarando map com chave-valor definidos.
nascimento := map [string] int{
	"felipe":25,
}

fmt.Println(nascimento)
}
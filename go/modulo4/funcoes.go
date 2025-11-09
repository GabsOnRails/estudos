//go:build ignore

package main

import (
	"fmt"
)

func main () {
	// soma(14,25) -> Não irá exibir o valor na tela
	resultadoSoma := soma(14,25) // Armazenando o resultado em uma variável.
	fmt.Println(resultadoSoma)

	nome,idade := cadastro("Gabriel",25)
	fmt.Println("Nome: "+nome+ "\nIdade: ",+idade)

}

func soma (x , y int) int {
	return x + y
}

func cadastro (name string, age int) (string, int) {
	return name, age
}

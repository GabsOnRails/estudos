//go:build ignore

package main

import (
	"fmt"
)

func main () {
	//Primeira forma de declarar var.
	var nome string
	nome = "Gabriel"
	fmt.Println(nome)

	//Declarando mais de uma var com o mesmo tipo.
	var a,b int
	a = 1
	b = 3
	fmt.Println(a)
	fmt.Println(b)

	//Segunda forma, usando a propriedade inferencia de tipo.
	var sobrenome = "oliveira"
	fmt.Println(sobrenome)

	//Terceira forma, mais utilizada.
	nacionalidade := "Brasileira"
	fmt.Println(nacionalidade)
	
	//Declarando uma constante, constantes usam inferencia de tipo.
	const idade = 25
	fmt.Println(idade)
	
}

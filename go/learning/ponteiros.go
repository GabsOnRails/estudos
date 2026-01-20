//go:build ignore

package main

import "fmt"

func alteraValor(i int) {
	i = 0
}

func alteraValorPonteiro(i *int) {
	*i = 0
}

func main() {
	i := 1
	fmt.Println("valor de i: ", i)
	fmt.Println("valor do endereco de memoria: ", &i)

	a := &i
	fmt.Println("valor de a: ", a)
	fmt.Println("valor de a*: ", *a) //para pegar o valor de &i
	fmt.Println("valor da memoria de a: ", &a)

	//Usando ponteiro
	alteraValor(i)
	fmt.Println("valor novo de i: ", i) //não altera
	alteraValorPonteiro(&i)
	fmt.Println("valor novo de i com ponteiro: ", i) //altera o valor direto
}

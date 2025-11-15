// Preciso pegar um número e retornar o negativo dele, se for 0, retorna 0 e se for negativo retorna o mesmo valor.
// A principio pensei em fazer uma funcao que pega o número, faz uma condicional (se maior que 0) e faz o cálculo.
// Pega o número, multiplica por dois e subtrai, ex 10 | 10x2 = 20 | 20 - 10 = -10.

package main

import "fmt"

func main () {
	fmt.Println(MakeNegative(10))
}


func MakeNegative(x int) int {
	if x <= 0 {
		return x
	} else {
		double := x * 2
		finalResult := x - double
		return finalResult
	}
}

// package kata_test
// import (
//   . "github.com/onsi/ginkgo"
//   . "github.com/onsi/gomega"
//   . "modulo5/returnNegative"
// )
// var _ = Describe("Test Example", func() {
//   It("should test that the solution returns the correct value", func() {
//     Expect(MakeNegative(42)).To(Equal(-42))
//   })
// })
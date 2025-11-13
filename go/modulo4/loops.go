//go:build ignore

package main

import (
	"fmt"
)

func main () {

	// sum := 0

	// for i := 0; i < 3; i ++ {
	// 	sum += i	
	// }
	// fmt.Println("Soma total: ",sum)

	// for j := 10; j >= 0; j -- {
	// 	fmt.Println(j)
	// }


	//Loop infinito
	// for {
	// 	fmt.Println("Go é top")
	// 	time.Sleep(2*time.Second)
	// }

	// For range -> Para percorrer uma lista

	frutas := []string{"Maça","Banana","Abacaxi","Goiaba"}

	for _, elementoFruta := range frutas {
		fmt.Println(elementoFruta)
	}


}


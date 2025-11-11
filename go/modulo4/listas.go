//go: build ignore

package main

import (
	"fmt"
)

func main () {
	//Array tamanho fixo

	var array [2] string
	array[0] = "Hello"
	array[1] = "World"
	
	fmt.Println(array[0])
	fmt.Println(array)

	//Outra forma de declarar array
	NumPrimos := [6] int{2,3,5,7,11,13}
	fmt.Println(NumPrimos[4]) // -> 11
	fmt.Println(NumPrimos[0:3]) // posição 0 até a 3, ou seja, a posição três não está inclusa.
	fmt.Println(NumPrimos[:3]) // Tudo que está antes da posição 3 - posição definida não está inclusa.
	fmt.Println(NumPrimos[2:]) // Tudo que está depois da posição 2 - posição definida estã inclusa.

	//Slice
	slice := make ([]string,5)
	slice[0] = "Gabriel"
	fmt.Println(slice)
	fmt.Println(len(slice))
	slice = append(slice, "Felipe")
	fmt.Println(slice)

	//Outra forma de declarar um slice
	sliceteste := []int{1,2,3,4,5,6}
	fmt.Println(sliceteste)
	sliceteste = append(sliceteste, 9)
	fmt.Print(sliceteste)
}
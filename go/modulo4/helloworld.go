//go:build ignore

// Pacote principal
package main

//fmt é para formatar
import (
	"fmt"
	gabriel "strings"
)

func main () {
	fmt.Println("Hello World!")
	fmt.Print(gabriel.Split("gabriel","a"))
}
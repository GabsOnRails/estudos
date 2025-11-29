// Given a string s, your task is to return another string such that even-indexed and odd-indexed letteracters of s are grouped and the groups are space-separated. Even-indexed group comes as first, followed by a space, and then by the odd-indexed part.

// Passos para o algoritmo.
// Precisarei percorrer todas as letras para pegar o index delas. Então usarei um for, mas isso não funciona em string, eu acho. Funciona, mas o value volta como rune então preciso converter isso em string letter := string(value). Depois fiz um if else para descobrir se o index é par ou impar e separar os valores em duas strings diferentes. Apos isso, usei o sprintf para formatar a string final da maneira que o exercicio pede.
package main

import (
	"fmt"
)

func main() {
	// fmt.Println(SortMyString("teste"))
}

func SortMyString(phrase string) string {
	var evenPhrase, oddPhrase, finalPhrase string
	for index, value := range phrase {
		letter := string(value)
		if index%2 == 0 {
			evenPhrase += string(letter)
			continue //quando a condição é != do passado, ele volta pro inicio do for, até acabarem os valores
		}
		oddPhrase += string(letter)

	}

	result := fmt.Sprintf("%s %s", evenPhrase, oddPhrase)
	finalPhrase += result

	return finalPhrase
}

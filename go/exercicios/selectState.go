//go:build ignore

package main

import "fmt"

func main() {
	paises := []string{"brasil", "holanda", "chile"}
	fmt.Print(retornaLetras(paises))

}

func retornaLetras(paises []string) ([]string, []string) {
	paiscoma := []string{}
	paissema := []string{}
	for _, pais := range paises {
		temA := false
		for _, char := range pais {
			if char == 'a' {
				temA = true
				break
			}
		}
		if temA {
			paiscoma = append(paiscoma, pais)
		} else {
			paissema = append(paissema, pais)
		}
	}
	return paiscoma, paissema
}

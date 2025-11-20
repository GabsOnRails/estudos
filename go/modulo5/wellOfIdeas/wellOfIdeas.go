// For every good kata idea there seem to be quite a few bad ones!
//
// In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

package main

func main() {

}

// vou precisar de um for para percorrer o slice, depois para cada valor igual a good vou somar em um contador, se o contador for maior que dois, retorno series, se for 1 ou || 2 retorno publish.
func Well(ideas []string) string {
	contador := 0
	phrase := ""

	for _, checkIdeas := range ideas {
		if checkIdeas == "good" {
			contador++
		}
		if contador > 2 {
			phrase = "I smell a series!"
		} else if contador == 1 || contador == 2 {
			phrase = "Publish!"
		} else {
			phrase = "Fail!"
		}
	}
	return phrase

}

// Dá pra usar o switch case também e faz mais sentido.

// func Well(ideas []string) string {
// 	counter := 0

// 	for _, checkIdeas := range ideas {
// 		if checkIdeas == "good" {
// 			counter++
// 		}
// 	}

// 	switch {
// 	case counter > 2:
// 		return "I smell a series!"
// 	case counter > 0: // seria entre 1 e 2 por conta do case acima
// 		return "Publish!"
// 	default:
// 		return "fail"
// 	}

// }

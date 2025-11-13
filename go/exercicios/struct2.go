//go:build ignore

package main

import (
	"fmt"
)

func main () {
	card1 := Card {
		CardNumber: 134576890,
		CardCode: 901,
		Name: "Gabriel",
		Authorize: false,
	}
	card1 = CheckCard(card1) //atribuindo novo valor ao card1 para alterar o authorize
	fmt.Print(Approve(card1)) //usando novo valor para chamar a func, caso contrário seria chamado o valor original e sempre retornaria false.
}

type Card struct {
	CardNumber int 
	CardCode int
	Name string
	Authorize bool
}

func NewCard (CardNumber, CardCode int, Name string) Card{
return Card {
	CardNumber: CardNumber,
	CardCode: CardCode,
	Name: Name,
}
}

func CheckCard (card Card) Card{
	if card.CardCode > 900 {
		card.Authorize = true // valor sendo alterado
	} 
	return card 
}

func Approve (card Card) string {
 if card.Authorize == true {
	fmt.Println("Approved Purchase!")
 } else {
	fmt.Println("Denied Purchase!")
 }
 return "Thank you and come back\n"
}

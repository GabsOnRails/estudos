// Rules of the "Rock, Paper, Scissors" game are:

// Rock beats Scissors,
// Scissors beat Paper,
// Paper beats Rock,
// Two identical moves are a draw.
// Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.

// Vou receber duas variaveis, se elas foram iguais irá retornar draw. Se a primeira for papel e a segunda for pedra. Papel ganha. Se for papel e a segunda tesoura, tesoura ganha. São sempre duas variações.
// Mas acho que tratar com if será muito moroso, ao menos que consiga usar o and
package main

func main() {}

func Rps(p1, p2 string) string {
	if p1 != p2 {
		if p1 == "rock" {
			if p2 == "scissors" {
				return "Player 1 won!"
			} else {
				return "Player 2 won!"
			}
		} else if p1 == "scissors" {
			if p2 == "paper" {
				return "Player 1 won!"
			} else {
				return "Player 2 won!"
			}
		} else {
			if p2 == "rock" {
				return "Player 1 won!"
			} else {
				return "Player 2 won!"
			}
		}
	}

	return "Draw!"
}

//outras solucoes

// Essa é genial, basicamente ele pega os dois valores m[a] e compara, se o valor de b for igual, então o p2 ganhou.
// func Rps(a, b string) string {
// 	var m = map[string]string{"rock": "paper", "paper": "scissors", "scissors": "rock"}
// 	fmt.Println("Chave:", a)
// 	fmt.Println("Valor da chave:", m[a])
// como eu passei como parametro "rock" e "paper", a = rock e m[a] = paper (valor que a chave tem no mapa M declarado na linha 13)

// 	if a == b {
// 		return "Draw!"
// 	}
// 	if m[a] == b {
// 		return "Player 2 won!"
// 	}
// 	return "Player 1 won!"
// }

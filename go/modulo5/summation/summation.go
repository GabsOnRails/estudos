package main

//preciso fazer uma funcao que retorne a soma dos valores, de 1 a 10, de forma agregrada (0+1+2+3+4+5+6+7+8+9+10). O 0 e 10 estao inclusos.
// Para fazer isso acredito que um loop junto de um incremento de valor deve resolver

import "fmt"

func main () {
	fmt.Println(summation(8))

}

func summation(x int) int{
	
	sum :=0
	for i := 0; i <=x; i ++{
		sum += i
		
	}
	 return sum
}
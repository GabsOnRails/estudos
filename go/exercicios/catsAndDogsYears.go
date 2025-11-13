//go: build ignore

package main

import "fmt"

// Eu preciso retornar a idade do cachorro e do gato seguindo as seguintes regras:
// Gato -> 1 ano valem 15 anos humanos.
// 2 ano valem 9 anos.
// 3 ano em diante valem 4 anos.
// Cachorro -> 1 ano valem 15 anos.
// 2 ano valem 9 anos.
// 3 ano em diante valem 5 anos.
// 3 anos para cima é só subtrair, o valor que sobra multiplicamos pela quantidade em anoes humanos e usamos o 2 e 1 padrão.

func main () {
	years:=10
	fmt.Println(CalculateYears(years))
	

}

func CalculateYears(years int) (result [3]int) {
  // Write your solution here
  if years <= 0 {
        return result
    }
    if years == 1 {
        return [3]int{1,15,15}
    }
    if years == 2 {
        return [3] int{2,24,24}
    }
    age := years - 2
    cat := 24 + age*4
    dog := 24 + age*5
	result = [3]int{years,cat,dog}
	return result
}
 

	


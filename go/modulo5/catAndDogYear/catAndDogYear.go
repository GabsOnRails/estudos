// I have a cat and a dog.

// I got them at the same time as kitten/puppy. That was humanYears years ago.

// Return their respective ages now as [humanYears,catYears,dogYears]

// NOTES:

// humanYears >= 1
// humanYears are whole numbers only
// Cat Years
// 15 cat years for first year
// +9 cat years for second year
// +4 cat years for each year after that
// Dog Years
// 15 dog years for first year
// +9 dog years for second year
// +5 dog years for each year after that

// Preciso retornar tres valores diferentes em um array [3]. Para os dois primeiros anos, a idade é igual, então só retorno o valor. Depois declaro variável e faco o calculo para retornar o valor correto.
package catAndDogYear

func CalculateYears(years int) (result [3]int) {
	switch years {
	case 1:
		return [3]int{1, 15, 15}
	case 2:
		return [3]int{2, 24, 24}
	default:
		catAge := 24 + ((years - 2) * 4)
		dogAge := 24 + ((years - 2) * 5)
		return [3]int{years, catAge, dogAge}
	}
}

package incrementer

func Incrementer(numbers []int) []int {
	newSlice := []int{}
	var newValue int
	for i, v := range numbers {
		newIndice := i + 1
		newValue = v + newIndice

		if newValue >= 10 {
			newValue = newValue % 10

			newSlice = append(newSlice, newValue)

		} else {

			newSlice = append(newSlice, newValue)
		}

	}
	return newSlice
}

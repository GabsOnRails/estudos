package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, time int) int {
	countLayers := 0
	newTime := 0
	if time == 0 {
		newTime = 2
	} else {
		newTime = time
	}
	for i := range layers {
		i++
		countLayers++
	}
	return countLayers * newTime

}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	sauce := 0.0
	noodles := 0
	for _, value := range layers {
		if value == "sauce" {
			sauce++
		} else if value == "noodles" {
			noodles++
		}
	}
	resultSauce := sauce * 0.2
	resultNoodles := noodles * 50
	return resultNoodles, resultSauce
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList []string, myList []string) []string {
	lastItemFriend := len(friendsList) - 1
	lastItemMine := len(myList) - 1
	getItem := friendsList[lastItemFriend]
	myList[lastItemMine] = getItem
	return myList
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantites []float64, numberOfPortions int) []float64 {
	portions := float64(numberOfPortions) / 2

	newQuantites := []float64{}

	for _, value := range quantites {
		newQuantites = append(newQuantites, value*portions)
	}

	return newQuantites
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.

package main

func main() {

}

// inviteMoreWomen evaluates if the number of men exceeds the number of women.
func inviteMoreWomen(guests []int) bool {
	var menCount, womenCount int
	// menCount and womenCount keep track of how many men and women are present.

	// Iterate through each guest.
	// Convention: 1 represents a man, -1 represents a woman.
	for _, guest := range guests {

		if guest == 1 {
			menCount++
		} else {
			womenCount++
		}
	}

	// If the number of men is greater, we need to invite more women.
	return menCount > womenCount
}

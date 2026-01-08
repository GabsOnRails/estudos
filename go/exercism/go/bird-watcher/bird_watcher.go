package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	var totalOfBirds int
	for _, count := range birdsPerDay {
		totalOfBirds += count
	}
	return totalOfBirds
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	var birdsPerWeek, firstDay, lastDay int

	firstDay = (week - 1) * 7
	lastDay = firstDay + 7

	for _, value := range birdsPerDay[firstDay:lastDay] {
		birdsPerWeek += value
	}

	return birdsPerWeek
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for i, count := range birdsPerDay {
		if i%2 == 0 {
			birdsPerDay[i] = count + 1
		}
	}
	return birdsPerDay
}

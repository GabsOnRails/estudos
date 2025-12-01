package cars

import "math"

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return (float64(productionRate) * successRate) / 100
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	sucessRateRound := math.Round(successRate)
	floatToInt := int(sucessRateRound)
	return ((productionRate * floatToInt) / 100) / 60

}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {

	if carsCount < 10 {
		expendProduction := carsCount * 10000
		// return the final value for production if carsCount is less than 10.
		return uint(expendProduction)
	} else {
		carIndividually := carsCount % 10
		ValueIndividually := carIndividually * 10000
		// Bring the value for  individual cars that we dont produce using the pricing group

		carInGroup := carsCount - carIndividually
		ValueInGroup := carInGroup * 9500
		// Bring the value for cars that we produce using pricing group

		FinalValue := ValueIndividually + ValueInGroup // Return the final value for cost of production.
		return uint(FinalValue)

	}

}

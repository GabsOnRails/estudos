// Package weather provides a function that return a forecast weather for your city.
package weather

var (
	// CurrentCondition show us the condition of weather now.
	CurrentCondition string
	// CurrentLocation is used for bring precision forecast weather.
	CurrentLocation string
)

// Forecast function will bring the current condition of weather for your city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}

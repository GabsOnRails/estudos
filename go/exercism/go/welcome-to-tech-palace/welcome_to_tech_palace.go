package techpalace

import (
	"fmt"
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	customerToUper := strings.ToUpper(customer)
	formatedString := fmt.Sprintf("Welcome to the Tech Palace, %s", customerToUper)
	return formatedString
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	line := strings.Repeat("*", numStarsPerLine)
	fancyString := fmt.Sprintf("%s\n%s\n%s", line, welcomeMsg, line)
	return fancyString

}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	removeStars := strings.ReplaceAll(oldMsg, "*", "")
	removeTrim := strings.TrimSpace(removeStars)
	return removeTrim
}

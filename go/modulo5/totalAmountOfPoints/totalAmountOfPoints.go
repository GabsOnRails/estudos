package main

import (
	"strconv"
	"strings"
)

func main() {
}

func Points(games []string) int {
	totalPoints := 0
	for _, game := range games {
		points := strings.Split(game, ":")
		home, _ := strconv.Atoi(points[0])
		visitant, _ := strconv.Atoi(points[1])

		if home > visitant {
			totalPoints += 3
		} else if home == visitant {
			totalPoints += 1
		}

	}
	return totalPoints
}

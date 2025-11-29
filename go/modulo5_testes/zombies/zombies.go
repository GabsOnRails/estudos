package main

import "fmt"

func main() {
	fmt.Println((Zombie_shootout(100, 10, 20)))

}

func Zombie_shootout(zombies, initialRange, ammo int) string {
	maxRound := initialRange * 2
	var zombiesKilled, round int
	phrase := ""

	for i := 0; i <= maxRound; i++ {
		if zombies == 0 && ammo >= 0 && maxRound >= round {
			phrase = fmt.Sprintf("You shot all %d zombies.", zombiesKilled)
			break
		} else if zombies > 0 && maxRound == round && ammo >= 0 {
			phrase = fmt.Sprintf("You shot %d zombies before being eaten: overwhelmed.", zombiesKilled)
			break
		} else if zombies > 0 && round <= maxRound && ammo <= 0 {
			phrase = fmt.Sprintf("You shot %d zombies before being eaten: ran out of ammo.", zombiesKilled)
			break
		}
		ammo--
		zombies--
		zombiesKilled++
		round++

	}
	return phrase
}

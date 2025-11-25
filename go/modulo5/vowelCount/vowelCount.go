// Return the number (count) of vowels in the given vowelWording.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input vowelWording will only consist of lower case letters and/or spaces.

//I need to count vowel in a vowelWording, for this I can use switch case with a for loop. But I learned that package string have a func for this.

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(GetCount("abacadraba"))
}

func GetCount(vowelWord string) (count int) {
	countVowel := 0
	for _, letters := range vowelWord {
		char := string(letters)
		if strings.ContainsAny(strings.ToLower(char), "aeiou") {
			countVowel++
		}
	}
	return countVowel
}

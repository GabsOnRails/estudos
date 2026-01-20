//go:build ignore

package main

import "fmt"

func main() {

	cat := Cat{
		color: "black",
		paws:  4,
		noise: "miau miau",
	}

	dog := Dog{
		color: "grey",
		paws:  5,
		noise: "ruf ruf",
	}
	makeNoise(cat)
	makeNoise(dog)
}

type Animal interface {
	Noise() string     //method
	NumberOfPaws() int //method

}

type Cat struct {
	color string
	paws  int
	noise string
}

type Dog struct {
	color string
	paws  int
	noise string
}

// cat function
func (c Cat) Noise() string {
	return c.noise
}

func (c Cat) NumberOfPaws() int {
	return c.paws
}

// dog function
func (d Dog) Noise() string {
	return d.noise
}

func (d Dog) NumberOfPaws() int {
	return d.paws
}

// This function will be used in all cases.
func makeNoise(animal Animal) {
	fmt.Println(animal.Noise())
}

package main

import "fmt"

func main() {
	SortMyString("adele")
}

func SortMyString(stringnew string) string {
	for _, nova := range stringnew {
		fmt.Println(nova)
	}

	return stringnew
}

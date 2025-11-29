// Imagine two rings with numbers on them. The inner ring spins clockwise (decreasing by 1 each spin) and the outer ring spins counter clockwise (increasing by 1 each spin). We start with both rings aligned on 0 at the top, and on each move we spin each ring one increment. How many moves will it take before both rings show the same number at the top again?

// The inner ring has integers from 0 to innerMax and the outer ring has integers from 0 to outerMax, where innerMax and outerMax are integers >= 1.

// Explication: I think i need two loops, for inner and for outer and works like that: if inner 2 and outer 3 the stpes are: inner 2 outer 1 | inner 1 outer 2 | inner 0 outer 3 | inner 2 outer 0 | inner 1 outer 1
// Outer starts in 1 and increasing 1. return to 0 end pass the max
// inner starts in max and decreasing 1 per turn. When pass 0 return to max.
package main

import "fmt"

func main() {
	fmt.Println(SpinningRings(2, 3))

}

func SpinningRings(innerMax, outerMax int) int {
	inner := 0
	outer := 0
	count := 0

	for {
		inner--
		outer++
		count++

		if inner < 0 {
			inner = innerMax
		}
		if outer > outerMax {
			outer = 0
		}
		if inner == outer {
			return count
		}
	}

}

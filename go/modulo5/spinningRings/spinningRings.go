// Imagine two rings with numbers on them. The inner ring spins clockwise (decreasing by 1 each spin) and the outer ring spins counter clockwise (increasing by 1 each spin). We start with both rings aligned on 0 at the top, and on each move we spin each ring one increment. How many moves will it take before both rings show the same number at the top again?

// The inner ring has integers from 0 to innerMax and the outer ring has integers from 0 to outerMax, where innerMax and outerMax are integers >= 1.

// Explication: I think i need two loops, for inner and for outer and works like that: if inner 2 and outer 3 the stpes are: inner 2 outer 1 | inner 1 outer 2 | inner 0 outer 3 | inner 2 outer 0 | inner 1 outer 1
// Outer starts in 1 and increasing 1. return to 0 end pass the max
// inner starts in max and decreasing 1 per turn. When pass 0 return to max.
package main

func main() {

}

func SpinningRings(innerMax, outerMax int) int {
	innerStart := innerMax
	outerStart := 1
	countingSping := 1

	for innerStart != outerStart {
		innerStart--
		outerStart++
		countingSping++
		if innerStart < 0 {
			innerStart = innerMax
		}
		if outerStart > outerMax {
			outerStart = 0
		}
	}
	return countingSping
}

// your code here

//go:build ignore

package kata

import (
	"fmt"
)


 func CloseCompare(a, b, margin float64) int {
  
 if margin <= 0 {
	if a != b {
		if a > b {
			return 1
		} else {
			return -1
		}
	} else {
		return 0
	}
 } else {
	if a > b {
		resultadoM := a-b
		if resultadoM > margin {
			return 1
		} else {
			return 0
		}
	} else {
		resultadoMe := b - a
		if resultadoMe > margin {
			return -1
		} else {
			return 0
		}
	}
 }
	

 }

func main () {
fmt.Println(CloseCompare(3.0, 5.0, 3.0))  // Output: 0
fmt.Println(CloseCompare(0.0, 5.0, 3.0))  // Output: 1
fmt.Println(CloseCompare(5.0, 1.0, 3.0))  // Output: -1
}


// Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. The function should return whether a is lower than, close to, or higher than b.

// Please note the following:

// When a is close to b, return 0.
// For this challenge, a is considered "close to" b if margin is greater than or equal to the absolute distance between a and b.

// Otherwise...

//     When a is less than b, return -1.

//     When a is greater than b, return 1.

// If margin is not given, treat it as if it were zero.

// Assume: margin >= 0

// Tip: Some languages have a way to make parameters optional.
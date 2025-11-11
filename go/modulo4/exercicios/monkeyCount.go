//go:build ignore

package exercicios

func monkeyCount(n int) []int {
	result := make([]int, n) // -> n is necessary for create a slice.
	for i := 0; i < n; i++ {
		result[i] = i + 1
	}
	return result
}
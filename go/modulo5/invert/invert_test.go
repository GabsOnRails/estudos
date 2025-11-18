package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func dotest(a []int, expected []int) {
	actual := Invert(append([]int{}, a...))
	if len(expected) == 0 {
		Expect(actual).To(BeEmpty(), "With arr = %v", a)
	} else {
		Expect(actual).To(Equal(expected), "With arr = %v", a)
	}
}

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		dotest([]int{1, 2, 3, 4, 5}, []int{-1, -2, -3, -4, -5})
		dotest([]int{1, -2, 3, -4, 5}, []int{-1, 2, -3, 4, -5})
		dotest(nil, nil)
		dotest([]int{0}, []int{0})
	})
})

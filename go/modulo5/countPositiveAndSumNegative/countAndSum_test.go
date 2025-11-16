package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Test Example", func() {
	It("should work for sample tests", func() {
		arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15}
		res := []int{10, -65}
		Expect(CountPositivesSumNegatives(arr)).To(Equal(res))
	})
})

var _ = Describe("Test Example", func() {
	It("should work for sample tests", func() {
		arr2 := []int{1, 2, 3, 4, 5, -14, -15}
		res := []int{5, -29}
		Expect(CountPositivesSumNegatives(arr2)).To(Equal(res))
	})
})

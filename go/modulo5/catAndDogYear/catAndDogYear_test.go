package catAndDogYear

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Sample tests", func() {
	It("one year", func() {
		Expect(CalculateYears(1)).To(Equal([3]int{1, 15, 15}))
	})

	It("two years", func() {
		Expect(CalculateYears(2)).To(Equal([3]int{2, 24, 24}))
	})

	It("ten years", func() {
		Expect(CalculateYears(10)).To(Equal([3]int{10, 56, 64}))
	})
})

package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		Expect(StantonMeasure([]int{1, 4, 3, 2, 1, 2, 3, 2})).To(Equal(3))
		Expect(StantonMeasure([]int{1, 4, 3, 0, 1, 9, 3, 6})).To(Equal(0))
	})
})

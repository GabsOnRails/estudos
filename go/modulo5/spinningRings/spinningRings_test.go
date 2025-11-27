package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Sample tests", func() {
	It("should handle basic cases", func() {
		Expect(SpinningRings(2, 3)).To(Equal(5))
		Expect(SpinningRings(3, 2)).To(Equal(2))
		Expect(SpinningRings(1, 1)).To(Equal(1))
		Expect(SpinningRings(2, 2)).To(Equal(3))
		Expect(SpinningRings(3, 3)).To(Equal(2))
	})
})

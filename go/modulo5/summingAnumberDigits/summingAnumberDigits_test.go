package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Basic tests", func() {
	It("Testing for fixed tests", func() {
		Expect(SumDigits(10)).To(Equal(1))
		Expect(SumDigits(99)).To(Equal(18))
		Expect(SumDigits(-32)).To(Equal(5))
	})
})

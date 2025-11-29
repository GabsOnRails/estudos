package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)


var _ = Describe("Test Example", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(MakeNegative(42)).To(Equal(-42))
  })
})
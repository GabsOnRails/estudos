package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func dotest(n int, expected string) {
	Expect(NumberToString(n)).To(Equal(expected), "With n = %d", n)
}

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		dotest(67, "67")
		dotest(79585, "79585")
		dotest(79585, "79585")
		dotest(3, "3")
		dotest(-1, "-1")
		dotest(0, "0")
	})
})

package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func dotest(s, expected string) {
	Expect(SortMyString(s)).To(Equal(expected), "With s = \"%s\"", s)
}

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		dotest("CodeWars", "CdWr oeas")
		dotest("YCOLUE'VREER", "YOU'RE CLEVER")
	})
})

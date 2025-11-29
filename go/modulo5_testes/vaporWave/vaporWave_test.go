package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func dotest(s, expected string) {
	Expect(Vaporcode(s)).To(Equal(expected), "With s = \"%s\"", s)
}

var _ = Describe("V  A  P  O  R  C  O  D  E", func() {
	It("Sample tests", func() {
		dotest("Lets go to the movies", "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
		dotest("Why isnt my code working", "W  H  Y  I  S  N  T  M  Y  C  O  D  E  W  O  R  K  I  N  G")
	})
})

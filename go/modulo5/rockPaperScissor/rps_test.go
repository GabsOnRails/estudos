package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		Expect(Rps("rock", "scissors")).To(Equal("Player 1 won!"))
		Expect(Rps("scissors", "rock")).To(Equal("Player 2 won!"))
		Expect(Rps("rock", "rock")).To(Equal("Draw!"))
	})
})

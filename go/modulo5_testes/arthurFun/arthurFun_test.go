package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Sample Test Cases:", func() {
	It("Should return the correct values for the sample test cases!", func() {
		Expect(inviteMoreWomen([]int{1, -1, 1})).To(Equal(true))
		Expect(inviteMoreWomen([]int{1, 1, 1})).To(Equal(true))
		Expect(inviteMoreWomen([]int{-1, -1, -1})).To(Equal(false))
		Expect(inviteMoreWomen([]int{1, -1})).To(Equal(false))
	})
})

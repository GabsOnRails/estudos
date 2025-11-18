package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Example Tests", func() {
	It("should repeat correctly", func() {
		Expect(RepeatStr(4, "a")).To(Equal("aaaa"))
		Expect(RepeatStr(3, "hello ")).To(Equal("hello hello hello "))
		Expect(RepeatStr(2, "abc")).To(Equal("abcabc"))
		Expect(RepeatStr(0, "")).To(Equal(""))
		Expect(RepeatStr(0, "I")).To(Equal(""))
		Expect(RepeatStr(5, "")).To(Equal(""))
		Expect(RepeatStr(6, "I")).To(Equal("IIIIII"))
		Expect(RepeatStr(5, "Hello")).To(Equal("HelloHelloHelloHelloHello"))
	})
})

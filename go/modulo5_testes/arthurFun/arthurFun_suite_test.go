package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestArthurFun(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "ArthurFun Suite")
}

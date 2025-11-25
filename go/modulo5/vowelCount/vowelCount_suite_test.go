package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestVowelCount(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "VowelCount Suite")
}

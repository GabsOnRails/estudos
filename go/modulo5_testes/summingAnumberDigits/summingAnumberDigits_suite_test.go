package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestSummingAnumberDigits(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "SummingAnumberDigits Suite")
}

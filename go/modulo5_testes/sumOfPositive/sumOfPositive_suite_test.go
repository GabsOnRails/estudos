package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestSumOfPositive(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "SumOfPositive Suite")
}

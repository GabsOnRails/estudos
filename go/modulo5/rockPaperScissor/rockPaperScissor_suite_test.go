package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestRockPaperScissor(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "RockPaperScissor Suite")
}

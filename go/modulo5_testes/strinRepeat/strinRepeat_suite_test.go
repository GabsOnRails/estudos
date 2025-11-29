package main

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestStrinRepeat(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "StrinRepeat Suite")
}

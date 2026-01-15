package incrementer

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestIncrementer(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Incrementer Suite")
}

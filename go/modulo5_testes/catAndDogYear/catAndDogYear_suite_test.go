package catAndDogYear

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestCatAndDogYear(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "CatAndDogYear Suite")
}

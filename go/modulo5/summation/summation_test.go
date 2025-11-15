package main

import (
	"fmt"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Basic Tests",func() {
    examples := [...][2]int{
        {1,1},
        {8,36},
        {22,253},
        {100,5050},
        {213,22791},
    }
    for i := 0; i < len(examples); i++ {
        v := examples[i]
        It(fmt.Sprintf("Testing for %d",v[0]),func() {
            Expect(summation(v[0])).To(Equal(v[1]))
        })
    }
})
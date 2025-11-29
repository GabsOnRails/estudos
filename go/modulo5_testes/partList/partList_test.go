package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func dotest(arr []string, exp string) {
	var ans = PartList(arr)
	Expect(ans).To(Equal(exp))
}

var _ = Describe("Tests PartList", func() {

	It("should handle basic cases", func() {
		dotest([]string{"I", "wish", "I", "hadn't", "come"},
			"(I, wish I hadn't come)(I wish, I hadn't come)(I wish I, hadn't come)(I wish I hadn't, come)")
		dotest([]string{"cdIw", "tzIy", "xDu", "rThG"},
			"(cdIw, tzIy xDu rThG)(cdIw tzIy, xDu rThG)(cdIw tzIy xDu, rThG)")

	})
})

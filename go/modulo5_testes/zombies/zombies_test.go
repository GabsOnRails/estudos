package main

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Basic tests", func() {
	It("Zombie_shootout(3, 10, 10)", func() { Expect(Zombie_shootout(3, 10, 10)).To(Equal("You shot all 3 zombies.")) })
	It("Zombie_shootout(100, 8, 200)", func() {
		Expect(Zombie_shootout(100, 8, 200)).To(Equal("You shot 16 zombies before being eaten: overwhelmed."))
	})
	It("Zombie_shootout(50, 10, 8)", func() {
		Expect(Zombie_shootout(50, 10, 8)).To(Equal("You shot 8 zombies before being eaten: ran out of ammo."))
	})
})

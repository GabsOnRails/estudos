package main

import (
	"fmt"
)
func main () {
	golf:= Car {Battery: 100, BatteryDrain: 5, Speed: 10, Distance:0}
	newDistance := Track {200}
	fmt.Println(CanFinish(golf,newDistance))
	}


	
	type Car struct {
		Battery int
		BatteryDrain int
		Speed int
		Distance int 
	}

	type Track struct {
		Distance int
	}

	
	func NewCar (Speed,BatteryDrain int) Car {
		return Car {
			Battery: 100,
			BatteryDrain: BatteryDrain,
			Speed: Speed,
			Distance: 0,
		}
	}

	func NewTrack (Distance int) Track {
		return Track {
			Distance: Distance,
		}
	}


	func Drive (car Car) Car {
		if car.Battery >= car.BatteryDrain {
			car.Distance += car.Speed
			car.Battery -= car.BatteryDrain
		}
		return car
	}

	func CanFinish (car Car, track Track) bool{
		totalDrive := car.Battery / car.BatteryDrain
		maxDistance := car.Speed * totalDrive

		return maxDistance >= track.Distance
	}
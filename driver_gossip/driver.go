package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"
)

// Driver asd
type Driver struct {
	secrets     map[int]bool
	id          int
	currentStop int
	route       []int
	stopCounter int
}

func main() {
	routes := [][]int{}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if len(scanner.Text()) == 0 {
			break
		}
		input := strings.Split(strings.Trim(scanner.Text(), " "), " ")
		route := make([]int, 0, len(input))
		for _, stop := range input {
			detour, _ := strconv.Atoi(stop)
			route = append(route, detour)
		}
		routes = append(routes, route)
	}

	drivers := initDrivers(routes)

	for _, driver := range drivers {
		fmt.Printf("Driver %d: secrets: %+v, currentStop: %+v, route: %+v, stopCounter: %d\n", driver.id, driver.secrets, driver.currentStop, driver.route, driver.stopCounter)
	}

	counter := 1
	for i := 1; i <= 480; i++ {
		if transferSecrets(drivers) {
			break
		}
		updateDrivers(drivers)
		counter++
	}

	for _, driver := range drivers {
		fmt.Printf("Driver %d: secrets: %+v, currentStop: %+v, route: %+v, stopCounter: %d\n", driver.id, driver.secrets, driver.currentStop, driver.route, driver.stopCounter)
	}

	if counter == 481 {
		fmt.Println("Never")
	} else {
		fmt.Println(counter)
	}

}

func initDrivers(routes [][]int) []*Driver {
	drivers := []*Driver{}

	for i, v := range routes {
		drivers = append(drivers, &Driver{
			secrets:     make(map[int]bool),
			id:          i,
			currentStop: v[0],
			route:       v,
			stopCounter: 0,
		})
		drivers[i].secrets[i] = true
	}
	return drivers
}

func transferSecrets(drivers []*Driver) bool {
	numSecrets := len(drivers)
	counter := 0
	for _, driver1 := range drivers {
		for _, driver2 := range drivers {
			if !reflect.DeepEqual(driver1, driver2) {
				gossip(driver1, driver2)
			}
		}
		if len(driver1.secrets) == numSecrets {
			counter++
		}
	}

	if counter == numSecrets {
		return true
	}
	return false
}

func gossip(driver1, driver2 *Driver) {
	if driver1.currentStop == driver2.currentStop {
		for s := range driver2.secrets {
			driver1.secrets[s] = true
		}
	}
}

func updateDrivers(drivers []*Driver) {
	for _, v := range drivers {
		v.stopCounter = (v.stopCounter + 1) % len(v.route)
		v.currentStop = v.route[v.stopCounter]
	}
}

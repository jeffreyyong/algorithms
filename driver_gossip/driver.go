package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Driver struct {
	Route  []string
	Gossip map[int]bool
	Stops  int
}

func simulate(routes [][]string, allStops map[string]bool) {
	drivers := make([]*Driver, 0, len(routes))
	for i := 0; i < len(routes); i++ {
		drivers = append(drivers,
			&Driver{
				Route:  routes[i],
				Gossip: map[int]bool{i: true},
				Stops:  0,
			})
	}

	stops := map[string][]*Driver{}
	for key := range allStops {
		stops[key] = make([]*Driver, 0, len(drivers))
	}

	for minute := 0; minute <= 60*8 + 1; minute++ {
		for _, driver := range drivers {
			stop := driver.Route[driver.Stops%len(driver.Route)]
			stops[stop] = append(stops[stop], driver)
		}

		for key := range stops {
			groupGossip := map[int]bool{}
			for _, driver := range stops[key] {
				for gossip := range driver.Gossip {
					groupGossip[gossip] = true
				}
			}
			for _, driver := range stops[key] {
				for gossip := range groupGossip {
					driver.Gossip[gossip] = true
				}
				driver.Stops++
			}

			stops[key] = make([]*Driver, 0, len(drivers))
		}

		done := true
		for _, driver := range drivers {
			if len(driver.Gossip) != len(drivers) {
				done = false
				break
			}
		}

		if done {
			fmt.Println("Done!", minute, "minutes.")
			return
		}
	}

	fmt.Println("Never.")
}

func main() {
	routes := [][]string{}
	stops := map[string]bool{}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if len(scanner.Text()) == 0 {
			break
		}
		input := strings.Split(strings.Trim(scanner.Text(), " "), " ")
		route := make([]string, 0, len(input))
		for _, stop := range input {
			route = append(route, stop)
			stops[stop] = true
		}
		routes = append(routes, route)
	}

	simulate(routes, stops)
}

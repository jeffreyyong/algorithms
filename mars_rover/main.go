package main

import (
	"bufio"
	"fmt"
	"os"

	"rover"
)

func main() {
	m := rover.Map{}
	m.SetDimensions(8, 8)

	ob := obstacle{point{2, 2}}
	ob1 := obstacle{point{2, 4}}
	m.obstacles = append(m.obstacles, ob, ob1)

	r1 := Rover{}
	r1.Init(0, 0, 0)

	runUserInputLoop()
}

func runUserInputLoop() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	command := scanner.Text()

	fmt.Println("Command: ", command)

	fmt.Println("Enter the command for the rover")

	r1.Command("ffrff")

}

func getCommand(scanner *bufio.Scanner) string {

}

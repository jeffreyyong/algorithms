package evil_hangman

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func runUserInput(words []string) {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Enter length of string")
	stringLen := getNextInt(scanner)

}

func main() {
	words, err := loadDictionary(os.Args[1])

	if err != nil {
		fmt.Println("Failed to load dictionary: " + err.Error())
		os.Exit(1)
	}

	runUserInput(words)
}

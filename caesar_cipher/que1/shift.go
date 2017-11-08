package main

import (
	// "bufio"
	"fmt"
	// "os"
	// "strconv"
	// "strings"
	// "unicode/utf8"
)

func shiftWord(cipherText string, shift int) string {
	toReturn := make([]byte, len(cipherText))
	for i, chr := range cipherText {
		num := 0
		if chr != ' ' {
			num = int(chr) + shift

			if num > 90 {
				num -= 26
			}

			if num < 65 {
				num += 26
			}

		}
		toReturn[i] = byte(num)
	}

	return string(toReturn)
}

//read text from command line and sanitize it
func getInput() (string, int) {

	// scanner := bufio.NewScanner(os.Stdin)
	// scanner.Scan()
	// cipherText := scanner.Text()
	// cipherText = strings.ToUpper(strings.TrimSpace(cipherText))
	// fmt.Println("You inserted: " + cipherText)
	// scanner.Scan()
	// shiftStr := scanner.Text()
	// shiftStr = strings.TrimSpace(shiftStr)
	// shiftInt, err := strconv.ParseInt(shiftStr, 10, 32)
	// if err != nil {
	// 	fmt.Println("Failed to get shift: ", err.Error())
	// }

	shiftInt := 2
	cipherText := "EFGH"
	// shiftInt = shiftInt % 26
	// if shiftInt < 26 {
	// 	shiftInt += 26
	// }

	return cipherText, shiftInt
}

func main() {
	cipherText, shift := getInput()
	fmt.Println(shiftWord(cipherText, shift))
}

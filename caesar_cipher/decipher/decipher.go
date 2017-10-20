package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//loads dictionary
func loadDictionary(path string) ([]string, error) {

	wordList := make([]string, 0)

	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		wordList = append(wordList, strings.ToUpper(strings.TrimSpace(scanner.Text())))
	}

	return wordList, nil
}

//split list into length-wise map
func splitByLen(words []string) map[int]([]string) {
	lenMap := make(map[int][]string)
	for _, word := range words {
		length := len(word)
		list, exists := lenMap[length]
		if exists {
			lenMap[length] = append(list, word)
		} else {
			lenMap[length] = []string{word}
		}

	}
	return lenMap
}

//finds allowed shift by matching ciphertext to dictionary
func getAllowedShifts(dictWords []string, cipherText string) []int {
	allowedShifts := []int{}
	length := len(cipherText)
	for _, word := range dictWords {
		i := 0
		for ; i < length; i++ {
			dictDiff := int(word[i]) - int(word[0])
			cipherDiff := int(cipherText[i]) - int(cipherText[0])
			if dictDiff < 0 {
				dictDiff += 26
			}
			if cipherDiff < 0 {
				cipherDiff += 26
			}

			if dictDiff != cipherDiff {
				break
			}
		}

		if i == length {
			allowedShift := int(word[0]) - int(cipherText[0])
			if allowedShift < 0 {
				allowedShift += 26
			}
			allowedShifts = append(allowedShifts, allowedShift)
		}
	}
	return allowedShifts
}

//find common elements of slice
func findCommon(slice1, slice2 []int) []int {
	common := map[int]bool{}
	commonSlice := []int{}
	for _, v := range slice1 {
		common[v] = false
	}
	for _, v := range slice2 {
		_, exists := common[v]
		if exists {
			common[v] = true
		}
	}

	for k, v := range common {
		if v {
			commonSlice = append(commonSlice, k)
		}
	}
	return commonSlice
}

func shiftWord(cipherText string, shift int) string {
	toReturn := make([]rune, len(cipherText))
	for i, chr := range cipherText {
		var num int = 0
		if chr != ' ' {
			num = int(chr) + shift

			if num > 90 {
				num -= 26
			}

			if num < 65 {
				num += 26
			}
			chr = rune(num)
		}
		toReturn[i] = chr
	}
	return string(toReturn)
}

//read text from command line and sanitize it
func getCipherText() string {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	cipherText := scanner.Text()
	cipherText = strings.ToUpper(strings.TrimSpace(cipherText))
	fmt.Println("You inserted: " + cipherText)
	return cipherText
}

func main() {

	dictWords, err := loadDictionary("./dictionary.txt")
	if err != nil {
		fmt.Printf("Failed to load dictionary %s \n", err.Error())
	}
	lenMap := splitByLen(dictWords)
	fmt.Println("Put some text:")
	cipherString := getCipherText()
	ciphers := strings.Split(cipherString, " ")
	allowedShifts := getAllowedShifts(lenMap[len(ciphers[0])], ciphers[0])
	for _, word := range ciphers[1:] {
		shifts := getAllowedShifts(lenMap[len(word)], word)
		allowedShifts = findCommon(allowedShifts, shifts)
		if len(allowedShifts) == 0 {
			break
		}
	}

	if len(allowedShifts) == 0 {
		fmt.Println("No match found ")
		return
	}

	fmt.Println("allowedShifts", allowedShifts)

	for _, shift := range allowedShifts {
		fmt.Println("Decoded:", shiftWord(cipherString, shift))
	}
}

package moneyconverter

import (
	"bufio"
	"fmt"
	"strings"
)

func init() {
	amountToWord = reverse(wordToAmount)
}

var (
	wordToAmount = map[string]int{
		"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
		"seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
		"thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
		"seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
		"forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
		"ninety": 90,
	}

	amountToWord map[int]string

	magnitudeToAmount = map[string]int{
		"thousand": 1000,
		"million":  1000000,
		"billion":  1000000000,
		"trillion": 1000000000000,
	}

	expToMagnitude = map[int]string{
		1: "thousand",
		2: "million",
		3: "billion",
		4: "trillion",
	}
)

func ParseWords(words string) (int, error) {
	scanner := bufio.NewScanner(strings.NewReader(words))
	scanner.Split(bufio.ScanWords)

	magnitudeSum := 0
	smallSum := 0
	for scanner.Scan() {
		token := scanner.Text()
		// fmt.Println(token)

		if i, found := wordToAmount[token]; found {
			smallSum += i
		} else if token == "hundred" {
			smallSum *= 100
		} else {
			if mag, found := magnitudeToAmount[token]; found {
				magnitudeSum += smallSum * mag
				smallSum = 0
			} else {
				if token == "and" || token == "dollars" || token == "dollar" {
					continue
				}
				return 0, fmt.Errorf("could not parse token: %s", token)
			}
		}
	}
	return magnitudeSum + smallSum, nil
}

func ToWords(amount int) string {
	if amount == 0 {
		return "zero dollars"
	}
	chunks := splitDigits(amount)
	// fmt.Printf("number chunks: %v\n", chunks)
	chunkWords := mapChunksToWords(chunks)
	// fmt.Printf("word chunks: %v\n", chunkWords)
	chunkWords = mapScales(chunkWords)
	fmt.Printf("word chunks with magnitude: %v\n", chunkWords)

	words := strings.Join(chunkWords, " ")

	if amount == 1 {
		return words + " dollar"
	}

	return words + " dollars"
}

func splitDigits(amount int) []int {
	chunks := make([]int, 0)
	for amount > 0 {
		chunks = append([]int{amount % 1000}, chunks...)
		amount = amount / 1000
	}
	return chunks
}

func mapChunksToWords(chunks []int) []string {
	words := make([]string, 0)
	for _, v := range chunks {
		words = append(words, amountToWords(v))
	}
	return words
}

func amountToWords(amount int) string {
	words := make([]string, 0)

	if amount == 0 {
		return ""
	}

	if amount < 20 {
		return amountToWord[amount]
	}

	if amount < 100 {
		ones := amount % 10 // Get the remaining number
		tens := amount / 10 // Get the numbers
		words = append(words, amountToWord[tens*10])
		if ones > 0 {
			words = append(words, amountToWord[ones])
		}
		return strings.Join(words, " ")
	}

	hundreds := amount / 100
	words = append(words, amountToWords(hundreds))
	words = append(words, "hundred")
	if amount%100 > 0 {
		words = append(words, "and", amountToWords(amount%100))
	}
	return strings.Join(words, " ")
}

func mapScales(chunks []string) []string {
	for i := 1; i < len(chunks); i++ {
		chunks[i] = expToMagnitude[len(chunks)-i] + " " + chunks[i]
		chunks[i] = strings.TrimSpace(chunks[i])
	}
	return chunks
}

func reverse(m map[string]int) map[int]string {
	n := make(map[int]string, len(m))
	for k, v := range m {
		n[v] = k
	}
	return n
}

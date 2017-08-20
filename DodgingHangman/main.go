package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func loadDictionary(filename string) ([]string, error) {
	fobj, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(fobj)
	words := []string{}
	for scanner.Scan() {
		word := scanner.Text()
		word = strings.TrimSpace(word)
		if word != "" {
			words = append(words, word)
		}
	}

	return words, nil
}

func filterByLen(words []string, length int) []string {

	tmpWords := []string{}
	for _, word := range words {
		if len(word) == length {
			tmpWords = append(tmpWords, word)
		}
	}

	return tmpWords
}

//assumes every word in "words" have same length
func commonCharacter(words []string) string {
	if len(words) == 0 {
		return ""
	}

	wordLen := len(words[0])
	toReturn := make([]byte, wordLen)
	for i := 0; i < wordLen; i++ {
		allHave := true
		c := words[0][i]

		for _, word := range words {
			if word[i] != c {
				allHave = false
				break
			}
		}
		if allHave {
			toReturn[i] = c
		} else {
			toReturn[i] = '_'
		}
	}
	return string(toReturn)
}

func getMaxPartition(c byte, words []string) (bool, []string) {

	wordLen := len(words[0])
	partitions := make(map[string][]string)
	emptyKey := make([]rune, wordLen)
	for i := 0; i < wordLen; i++ {
		emptyKey[i] = '_'
	}
	for _, word := range words {
		key := make([]rune, wordLen)
		copy(key, emptyKey)
		for i := 0; i < wordLen; i++ {
			if word[i] == c {
				key[i] = rune(c)
			}
		}
		keyStr := string(key)
		if partitions[keyStr] == nil {
			partitions[keyStr] = []string{word}
		} else {
			partitions[keyStr] = append(partitions[keyStr], word)
		}
	}

	maxPartitonKey := string(emptyKey)
	maxPartionLen := len(partitions[maxPartitonKey])
	for k, partition := range partitions {
		if len(partition) > maxPartionLen {
			maxPartionLen = len(partition)
			maxPartitonKey = k
		}
	}

	return (maxPartitonKey != string(emptyKey)), partitions[maxPartitonKey]

}

func getNextInt(scanner *bufio.Scanner) int {
	for {
		scanner.Scan()
		lenStr := scanner.Text()
		lenInt, err := strconv.ParseInt(lenStr, 10, 32)
		if err != nil {
			fmt.Println("Failed to parse int: ", err.Error())
			fmt.Println("Enter again")
		} else {
			return int(lenInt)
		}
	}
}

func getNextChar(scanner *bufio.Scanner) byte {
	for {
		scanner.Scan()
		str := scanner.Text()
		strings.TrimSpace(str)
		if len(str) != 1 {
			fmt.Println("Bad character "+str, " Enter again: ")
		} else {
			return str[0]
		}
	}

}

func stringContains(c rune, w string) bool {
	for _, p := range w {
		if p == c {
			return true
		}
	}
	return false
}

func runUserInputLoop(words []string) {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Enter length of string")
	stringLen := getNextInt(scanner)
	tmpWords := filterByLen(words, stringLen)
	for len(tmpWords) == 0 {
		fmt.Printf("No word of length %d exists \n ", stringLen)
		fmt.Println("Enter length of string")
		stringLen := getNextInt(scanner)
		tmpWords = filterByLen(words, stringLen)

	}
	words = tmpWords
	fmt.Println("Words are ")
	for _, word := range words {
		fmt.Println("(" + word + ")")
	}
	outWordByteArr := make([]byte, stringLen)
	for i := 0; i < stringLen; i++ {
		outWordByteArr[i] = '_'
	}

	outWord := string(outWordByteArr)
	chancesLeft := 10
	usedLetters := ""
	for chancesLeft > 0 {
		fmt.Printf("You have \t%d guesses left\n ", chancesLeft)
		fmt.Printf("Used letters are %s \n", usedLetters)
		fmt.Printf("Word: \t %s\n", outWord)
		fmt.Printf("Enter guess: ")
		c := getNextChar(scanner)
		if stringContains(rune(c), usedLetters) {
			fmt.Println("You have already used it ")
			continue
		}
		usedLetters = usedLetters + string(c)

		rightGues := false
		rightGues, words = getMaxPartition(c, words)
		fmt.Println(words)
		if !rightGues {
			fmt.Printf("Sorry, there are no %c\n", c)
			chancesLeft--
		} else {
			fmt.Println("Yey, Your guess is correct")
			outWord = commonCharacter(words)
			if !stringContains('_', outWord) {
				fmt.Println("You have won")
				fmt.Println("Correct word is " + outWord)
				return
			}
		}

	}
	fmt.Println(":( You lost")

}

func main() {
	words, err := loadDictionary(os.Args[1])

	if err != nil {
		fmt.Println("Failed to load dict: " + err.Error())
		os.Exit(1)
	}

	runUserInputLoop(words)
}

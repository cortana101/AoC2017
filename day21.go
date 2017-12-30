package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"os"
)

type art [][]bool

func (a art)splitArt() [][]art {
	if len(a) % 2 != 0 {
		panic("Cannot split uneven art")
	}
	split_size := len(a) / 2
	for i := 0; i <= split_size; i++ {
		for j := 0; j <= split_size; j++ {
			// Fill in the split
		}
	}
}

func getStartingArt() art {
	a := make(art, 3)
	a[0] = []bool{false, true, false}
	a[1] = []bool{false, false, true}
	a[2] = []bool{true, true, true}
	return a
}

func main() {
	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic("Cannot read file")
	}
	rules := strings.Split(string(dat), "\n")
	fmt.Println(rules)
}

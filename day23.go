package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"strconv"
	"os"
)

func prettyPrintRegs(regs map[rune]int) {
	for _, k := range []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'} {
		fmt.Printf("%s: %v, ", string(k), regs[k])
	}
	fmt.Printf("\n")
}

func getVal(val string, regs map[rune]int) int {
	val = strings.TrimSpace(val)
	i, err := strconv.Atoi(val)
	if err == nil {
		return i
	}
	targetRune := rune(val[0])
	addTargetIfNotExists(targetRune, regs)
	return regs[targetRune]
}

func addTargetIfNotExists(target rune, regs map[rune]int) {
	_, found := regs[target]
	if !found {
		regs[target] = 0
	}
}

func processCmds(cmds []string, regs map[rune]int) {
	mulCounter := 0
	instCounter := 0
	for i := 0 ; i < len(cmds) && i >= 0;{
		instCounter++
		if instCounter % 1000000 == 0 {
			fmt.Println(instCounter)
		}
		cmd := cmds[i]
		args := strings.Split(cmd, " ")
		target := rune(args[1][0])
		addTargetIfNotExists(target, regs)
		var val int
		if len(args) > 2 {
			val = getVal(args[2], regs)
		}
		if args[0] == "set" {
			if target == 'e' {
				prettyPrintRegs(regs)
			}
			regs[target] = val
		} else if args[0] == "sub" {
			if target == 'h' {
				fmt.Println(regs)
			}
			regs[target] -= val
		} else if args[0] == "mul" {
			mulCounter++
			regs[target] *= val
		} else if args[0] == "jnz" {
			val2 := getVal(args[1], regs)
			if val2 != 0 {
				i += val
				continue
			}
		}
		i++
	}
	fmt.Println("RegH", regs['h'])
	panic("We've run out of command positions.")
}


func main() {
	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic("Cannot read file")
	}
	lines := strings.Split(string(dat), "\n")
	fmt.Println(lines)
	regs := make(map[rune]int)
	regs['a'] = 1
	processCmds(lines, regs)
}

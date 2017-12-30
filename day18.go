package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"os"
	"strconv"
)

func addTargetIfNotExists(target rune, regs map[rune]int) {
	_, found := regs[target]
	if !found {
		regs[target] = 0
	}
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

func fakeProcessCmd(rcv chan int, snd chan int){
	for {
		select {
		case val := <- rcv:
			fmt.Println("Received a", val)
		}
	}
}

// Maybe make a queue type that synchronizes between 
type channeledQueue struct {
	buf []int
}

func (cq *channeledQueue)execute(write <-chan int) (read chan int) {
	for {
		select {
		case val := <- write:
			cq.buf = append(cq.buf, val)
		case read <- cq.buf[0]:
			cq.buf = cq.buf[1:]
		}
	}
}

func processCmds(cmds []string, regs map[rune]int, rcv chan int, snd chan int) {
	var sndBuf []int
	totalSends := 0
	for i := 0 ; i < len(cmds) && i >= 0;{
		if len(sndBuf) > 0 {
			select {
			case snd <- sndBuf[0]:
				sndBuf = sndBuf[1:]
				continue
			default:
				// Do nothing, just fall through and make the send a non-blocking op
			}
		}
		if totalSends % 1000 == 0 {
			fmt.Println(totalSends)
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
			regs[target] = val
		} else if args[0] == "add" {
			regs[target] += val
		} else if args[0] == "mul" {
			regs[target] *= val
		} else if args[0] == "mod" {
			regs[target] %= val
		} else if args[0] == "jgz" {
			if regs[target] > 0 {
				i += val
				continue
			}
		} else if args[0] == "snd" {
			sndBuf = append(sndBuf, regs[target])
			totalSends++
		} else if args[0] == "rcv" {
			if len(sndBuf) > 0 {
				continue
			} else {
				regs[target] = <- rcv
			}
		}
		i++
	}
	fmt.Println("Total sends:", totalSends)
	panic("We've run out of command positions.")
}

func run(cmds []string) {
	regZero := make(map[rune]int)
	regZero['p'] = 0
	regOne := make(map[rune]int)
	regOne['p'] = 1
	sndZero := make(chan int)
	sndOne := make(chan int)
	rcvZero := make(chan int)
	rcvOne := make(chan int)
	go processCmds(cmds, regZero, rcvZero, sndZero)
	go processCmds(cmds, regOne, rcvOne, sndOne)
	var val int
	oneSends := 0
	for {
		select {
		case val = <- sndZero:
			rcvOne <- val
		case val = <- sndOne:
			oneSends++
			fmt.Println("OneSends:", oneSends)
			rcvZero <- val
		}
	}
}

func main() {
	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic("Cannot read file")
	}
	cmds := strings.Split(string(dat), "\n")
	run(cmds)
}

package main

import (
	"fmt"
)

type stateFunction func(map[int]bool, int) (int, stateFunction)

func addIfNotExists(tape map[int]bool, cursor int) {
	_, ok := tape[cursor] 
	if !ok {
		tape[cursor] = false
	}
}

func stateF(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	if !tape[cursor] {
		tape[cursor] = false
		cursor++
		nextStep = stateC
	} else {
		tape[cursor] = false
		cursor++
		nextStep = stateE
	}
	return cursor, nextStep
}

func stateE(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	if !tape[cursor] {
		tape[cursor] = true
		cursor--
		nextStep = stateA
	} else {
		tape[cursor] = false
		cursor++
		nextStep = stateB
	}
	return cursor, nextStep
}

func stateD(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	if !tape[cursor] {
		tape[cursor] = false
		cursor--
		nextStep = stateE
	} else {
		tape[cursor] = true
		cursor++
		nextStep = stateA
	}
	return cursor, nextStep
}

func stateC(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	if !tape[cursor] {
		tape[cursor] = true
		cursor--
		nextStep = stateC
	} else {
		tape[cursor] = true
		cursor--
		nextStep = stateA
	}
	return cursor, nextStep
}

func stateB(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	if !tape[cursor] {
		tape[cursor] = true
		cursor++
		nextStep = stateC
	} else {
		tape[cursor] = false
		cursor++
		nextStep = stateF
	}
	return cursor, nextStep
}

func stateA(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	addIfNotExists(tape, cursor)
	if !tape[cursor] {
		tape[cursor] = true
		cursor++
		nextStep = stateB
	} else {
		tape[cursor] = false
		cursor--
		nextStep = stateD
	}
	return cursor, nextStep
}

func shortStateB(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	addIfNotExists(tape, cursor)
	if !tape[cursor] {
		tape[cursor] = true
		cursor--
		nextStep = shortStateA
	} else {
		tape[cursor] = true
		cursor++
		nextStep = shortStateA
	}
	return cursor, nextStep
}

func shortStateA(tape map[int]bool, cursor int) (nextCursor int, nextStep stateFunction) {
	addIfNotExists(tape, cursor)
	if !tape[cursor] {
		tape[cursor] = true
		cursor++
		nextStep = shortStateB
	} else {
		tape[cursor] = false
		cursor--
		nextStep = shortStateB
	}
	return cursor, nextStep
}

func getCheckSum(tape map[int]bool) int {
	total := 0
	for _, v := range tape {
		if v {
			total++
		}
	}
	return total
}

func main() {
	tape := make(map[int]bool)
	cursor := 0
	step_limit := 12302209 
	// step_limit := 6
	// stateToRun := shortStateA
	stateToRun := stateA
	for i := 0; i < step_limit; i++ {
		cursor, stateToRun = stateToRun(tape, cursor)
	}
	checkSum := getCheckSum(tape)
	fmt.Println(checkSum)
}
package main

import (
	"strconv"
	"fmt"
	"strings"
	"io/ioutil"
	"os"
)

type component struct {
	ports []int
}

func (c component)serialize() string {
	return fmt.Sprintf("%v", c.ports)
}

func getComponent(line string) component {
	bits := strings.Split(line, "/")
	if len(bits) != 2 {
		panic("Wrong length component entry")
	}
	var comp component
	for _, b := range bits {
		b = strings.TrimSpace(b)
		val, err := strconv.Atoi(b)
		if err != nil {
			panic(fmt.Sprintln("There is an error parsing a value", err))
		}
		comp.ports = append(comp.ports, val)
	}
	return comp
}

func isInList(comp component, comps []component) bool {
	for _, c := range comps {
		if comp.serialize() == c.serialize() {
			return true
		}
	}
	return false
}

func getAvailablePart(comp1, comp2 component) (int, error) {
	if comp1.ports[0] == comp2.ports[0] {
		return comp2.ports[1], nil
	} else if comp1.ports[0] == comp2.ports[1] {
		return comp2.ports[0], nil
	} else if comp1.ports[1] == comp2.ports[0] {
		return comp2.ports[1], nil
	} else if comp1.ports[1] == comp2.ports[1] {
		return comp2.ports[0], nil
	} else {
		return 0, fmt.Errorf("no match found")
	}
}

func getStrength(comps []component) int {
	strength := 0
	for _, c := range comps {
		strength += c.ports[0] + c.ports[1]
	}
	return strength
}

func getMaxStrength(comps []component, accum []component) (maxStrength, length int) {
	maxSubStrength := 0
	maxLength := 0
	var requiredPort int
	var err error
	if len(accum) == 0 {
		requiredPort = 0
	} else if len(accum) == 1 {
		requiredPort = accum[0].ports[1]
	} else {
		requiredPort, err = getAvailablePart(accum[len(accum) - 2], accum[len(accum) - 1])		
		if err != nil {
			panic("This should never happen")
		}
	}
	accumLength := len(accum)
	for i, c := range comps {
		if accumLength < 3 {
			fmt.Println("i", i, "depth:", accumLength)
		}
		if c.ports[0] == requiredPort || c.ports[1] == requiredPort {
			newAccum := append(accum, c)
			newComp := make([]component, len(comps))
			copy(newComp, comps)
			newComp = append(newComp[:i], newComp[i + 1:]...)
			subStrength, subLength := getMaxStrength(newComp, newAccum)
			if subLength > maxLength {
				maxSubStrength = subStrength
				maxLength = subLength
			} else if subLength == maxLength {
				if subStrength > maxSubStrength {
					maxSubStrength = subStrength
				}
			}
		}
	}
	if maxSubStrength == 0 {
		return getStrength(accum), accumLength
	}
	return maxSubStrength, maxLength
}

func main() {
	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic("Cannot read file")
	}
	lines := strings.Split(string(dat), "\n")
	var comps []component
	for _, l := range lines {
		comps = append(comps, getComponent(l))
	}
	var accum []component
	maxStrength, maxLength := getMaxStrength(comps, accum)
	fmt.Println("Maxstrength is", maxStrength, "maxlength is", maxLength)
}

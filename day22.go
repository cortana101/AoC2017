package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"os"
)

type direction struct {
	x, y int
}

func (d direction)turnAround() direction {
	// left is 2 rights
	d = d.turnRight()
	d = d.turnRight()
	return d
}

func (d direction)turnLeft() direction {
	// left is 3 rights
	d = d.turnRight()
	d = d.turnRight()
	d = d.turnRight()
	return d
}

func (d direction)turnRight() direction {
	if d.x == 1 {
		d.x = 0
		d.y = 1
	} else if d.y == 1 {
		d.x = -1
		d.y = 0
	} else if d.x == -1 {
		d.x = 0
		d.y = -1
	} else if d.y == -1 {
		d.x = 1
		d.y = 0
	} else {
		panic("We really messed up the directions")
	}
	return d
}

type infmap struct {
	data map[string]rune
	minx, miny, maxx, maxy int
}

func encodeKey(x, y int) string {
	key := fmt.Sprintf("%d,%d", x, y)
	return key
}

func (im *infmap)setBoundingBox(x, y int) {
	if x < im.minx {
		im.minx = x
	} else if x > im.maxx {
		im.maxx = x
	}
	if y < im.miny {
		im.miny = y
	} else if y > im.maxy {
		im.maxy = y
	}
}

func (im *infmap)getVal(x, y int) rune {
	im.setBoundingBox(x, y)
	key := encodeKey(x, y)
	val, ok := im.data[key]
	if !ok {
		im.data[key] = '.'
		return '.'
	}
	return val
}

func (im *infmap)setVal(x, y int, val rune) {
	im.setBoundingBox(x, y)
	key := encodeKey(x, y)
	im.data[key] = val
}

func (im *infmap)initFromFile(lines []string) {
	im.minx = 0
	im.miny = 0
	im.maxx = 0
	im.maxy = 0
	im.data = make(map[string]rune)
	for y, l := range lines {
		if y > im.maxy {
			im.maxy = y
		}
		l = strings.TrimSpace(l)
		for x, c := range l {
			if x > im.maxx {
				im.maxx = x
			}
			im.setVal(x, y, c)
		}
	}
}

func (im *infmap)printMap() {
	for y := im.miny; y <= im.maxy; y++ {
		for x := im.minx; x <= im.maxx; x++ {
			fmt.Printf(string(im.getVal(x, y)))
		}
		fmt.Printf("\n")
	}
}

func runVirus(im infmap, cycles int) (infmap, int) {
	x := (im.maxx - im.minx) / 2
	y := (im.maxy - im.miny) / 2
	d := direction{x: 0, y: -1}
	infects := 0
	for i := 0; i < cycles; i++ {
		val := im.getVal(x, y)
		if val == '#' {
			d = d.turnRight()
			im.setVal(x, y, 'F')
		} else if val == 'F' {
			im.setVal(x, y, '.')
			d = d.turnAround()
		} else if val == '.' {
			im.setVal(x, y, 'W')
			d = d.turnLeft()
		} else if val == 'W' {
			infects++
			im.setVal(x, y, '#')
		}
		x += d.x
		y += d.y
	}
	return im, infects
}

func main() {
	dat, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic("Cannot read file")
	}
	lines := strings.Split(string(dat), "\n")
	var im infmap
	var infects int
	im.initFromFile(lines)
	im, infects = runVirus(im, 10000000)
	// im.printMap()
	fmt.Println("Infects:", infects)
}
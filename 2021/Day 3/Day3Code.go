package main

import (
	"fmt"
	"funk"
	"os"
	"strconv"
	"strings"
)

func part1() {
	inp, _ := os.ReadFile("Day3input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	eps := ""
	gam := ""
	for i := 0; i < 12; i++ {
		c0 := 0
		c1 := 0
		for _, l := range f {
			if l[i] == '1' {
				c1++
			} else {
				c0++
			}
		}
		if c0 > c1 {
			gam += "0"
			eps += "1"
		} else {
			gam += "1"
			eps += "0"
		}
	}
	a, _ := strconv.ParseInt(gam, 2, 32)
	b, _ := strconv.ParseInt(eps, 2, 32)
	fmt.Println(a * b)
}

func part2() {
	inp, _ := os.ReadFile("Day3input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	oxy := make([]string, len(f))
	co2 := make([]string, len(f))
	copy(oxy, f)
	copy(co2, f)
	for i := 0; i < 12; i++ {
		c0 := 0
		c1 := 0
		for _, l := range oxy {
			if l[i] == '1' {
				c1++
			} else {
				c0++
			}
		}
		if len(oxy) > 1 {
			if c0 > c1 {
				oxy = (funk.Filter(oxy, func(x string) bool { return x[i] == '0' })).([]string)
			} else {
				oxy = (funk.Filter(oxy, func(x string) bool { return x[i] == '1' })).([]string)
			}
		}
		c0 = 0
		c1 = 0
		for _, l := range co2 {
			if l[i] == '1' {
				c1++
			} else {
				c0++
			}
		}
		if len(co2) > 1 {
			if c0 > c1 {
				co2 = (funk.Filter(co2, func(x string) bool { return x[i] == '1' })).([]string)
			} else {
				co2 = (funk.Filter(co2, func(x string) bool { return x[i] == '0' })).([]string)
			}
		}
	}
	a, _ := strconv.ParseInt(oxy[0], 2, 32)
	b, _ := strconv.ParseInt(co2[0], 2, 32)
	fmt.Println(a * b)
}

func main() {
	part1()
	part2()
}

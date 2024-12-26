package main

import (
	"fmt"
	"funk"
	"os"
	"strconv"
	"strings"
)

func reader() []string {
	inp, _ := os.ReadFile("input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	return f
}

func cache(f func(int, int) int) func(int, int) int {
	Memo := [500][500]int{}
	res := func(x int, y int) int {
		if Memo[x][y] == 0 {
			Memo[x][y] = f(x, y)
		}
		return Memo[x][y]
	}
	return res
}

func part1() {
	f := reader()
	timers := funk.Map(strings.Split(f[0], ","), func(s string) int { a, _ := strconv.ParseInt(s, 10, 32); return int(a) }).([]int)
	var simulate func(int, int) int
	simulate = cache(func(n int, t int) int {
		if t <= 0 {
			return 1
		}
		if n == 0 {
			return simulate(6, t-1) + simulate(8, t-1)
		}
		return simulate(n-1, t-1)
	})
	s := 0
	for _, t := range timers {
		s += simulate(t, 80)
	}
	fmt.Println(s)
}

func part2() {
	f := reader()
	timers := funk.Map(strings.Split(f[0], ","), func(s string) int { a, _ := strconv.ParseInt(s, 10, 32); return int(a) }).([]int)
	var simulate func(int, int) int
	simulate = cache(func(n int, t int) int {
		if t <= 0 {
			return 1
		}
		if n == 0 {
			return simulate(6, t-1) + simulate(8, t-1)
		}
		return simulate(n-1, t-1)
	})
	s := 0
	for _, t := range timers {
		s += simulate(t, 256)
	}
	fmt.Println(s)
}

func main() {
	part1()
	part2()
}

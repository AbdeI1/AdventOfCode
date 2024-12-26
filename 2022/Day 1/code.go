package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func reader() []string {
	inp, _ := os.ReadFile("input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	return f
}

func part1() {
	f := reader()
	ans, s := -1, 0
	for _, l := range f {
		if l == "" {
			ans = int(math.Max(float64(ans), float64(s)))
			s = 0
			continue
		}
		i, _ := strconv.ParseInt(l, 10, 32)
		s += int(i)
	}
	fmt.Println(ans)
}

func part2() {
	f := reader()
	var a []int
	s := 0
	for _, l := range f {
		if l == "" {
			a = append(a, s)
			s = 0
			continue
		}
		i, _ := strconv.ParseInt(l, 10, 32)
		s += int(i)
	}
	sort.Slice(a, func(i, j int) bool {
		return a[i] > a[j]
	})
	fmt.Println(a[0] + a[1] + a[2])
}

func main() {
	part1()
	part2()
}

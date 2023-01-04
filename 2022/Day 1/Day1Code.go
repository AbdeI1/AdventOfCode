package main

import (
	"fmt"
	"os"
	"strings"
)

func reader() []string {
	inp, _ := os.ReadFile("Day1input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	return f
}

func part1() {
	f := reader()
	fmt.Println(f)
}

func part2() {
	f := reader()
	fmt.Println(f)
}

func main() {
	part1()
	part2()
}

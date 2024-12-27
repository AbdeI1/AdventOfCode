package main

import (
	"fmt"
	"funk"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
)

func reader() []string {
	_, path, _, _ := runtime.Caller(0)
	os.Chdir(filepath.Dir(path))
	inp, _ := os.ReadFile("input.txt")
	f := strings.Split(string(inp), "\n")
	f = f[:len(f)-1]
	return f
}

func part1() {
	f := reader()
	nums := funk.Map(strings.Split(f[0], ","), func(s string) int32 { r, _ := strconv.ParseInt(s, 10, 32); return int32(r) }).([]int32)
	boards := [100][5][5]int32{}
	i := -1
	j := 0
	for _, l := range f[1:] {
		if len(l) == 0 {
			i++
			j = 0
			continue
		}
		line := strings.Split(l, " ")
		lk := 0
		for k := 0; k < 5; k++ {
			if line[lk] == "" {
				lk++
			}
			t, _ := strconv.ParseInt(line[lk], 10, 32)
			boards[i][j][k] = int32(t)
			lk++
		}
		j++
	}
	for _, n := range nums {
		for k := 0; k < len(boards); k++ {
			for i := 0; i < len(boards[k]); i++ {
				for j := 0; j < len(boards[k][i]); j++ {
					if boards[k][i][j] == n {
						boards[k][i][j] = -1
						cn1 := 0
						for l := 0; l < 5; l++ {
							if boards[k][i][l] == -1 {
								cn1++
							}
						}
						if cn1 >= 5 {
							var s int32 = 0
							for r := range boards[k] {
								for _, v := range boards[k][r] {
									if v != -1 {
										s += v
									}
								}
							}
							fmt.Println(s * n)
							return
						}
						cn1 = 0
						for l := 0; l < 5; l++ {
							if boards[k][l][j] == -1 {
								cn1++
							}
						}
						if cn1 >= 5 {
							var s int32 = 0
							for r := range boards[k] {
								for _, v := range boards[k][r] {
									if v != -1 {
										s += v
									}
								}
							}
							fmt.Println(s * n)
							return
						}
					}
				}
			}
		}
	}
	fmt.Println("bad")
}

func part2() {
	f := reader()
	nums := funk.Map(strings.Split(f[0], ","), func(s string) int32 { r, _ := strconv.ParseInt(s, 10, 32); return int32(r) }).([]int32)
	boards := [100][5][5]int32{}
	i := -1
	j := 0
	for _, l := range f[1:] {
		if len(l) == 0 {
			i++
			j = 0
			continue
		}
		line := strings.Split(l, " ")
		lk := 0
		for k := 0; k < 5; k++ {
			if line[lk] == "" {
				lk++
			}
			t, _ := strconv.ParseInt(line[lk], 10, 32)
			boards[i][j][k] = int32(t)
			lk++
		}
		j++
	}
	bw := 0
	for _, n := range nums {
		for k := 0; k < len(boards); k++ {
			for i := 0; i < len(boards[k]); i++ {
				for j := 0; j < len(boards[k][i]); j++ {
					if boards[k][i][j] == n {
						boards[k][i][j] = -1
						cn1 := 0
						for l := 0; l < 5; l++ {
							if boards[k][i][l] == -1 {
								cn1++
							}
						}
						if cn1 >= 5 && bw >= 99 {
							var s int32 = 0
							for r := range boards[k] {
								for _, v := range boards[k][r] {
									if v != -1 {
										s += v
									}
								}
							}
							fmt.Println(s * n)
							return
						} else if cn1 >= 5 {
							for r := 0; r < len(boards[k]); r++ {
								for c := 0; c < len(boards[k][r]); c++ {
									boards[k][r][c] = -1
								}
							}
							bw++
							continue
						}
						cn1 = 0
						for l := 0; l < 5; l++ {
							if boards[k][l][j] == -1 {
								cn1++
							}
						}
						if cn1 >= 5 && bw >= 99 {
							var s int32 = 0
							for r := range boards[k] {
								for _, v := range boards[k][r] {
									if v != -1 {
										s += v
									}
								}
							}
							fmt.Println(s * n)
							return
						} else if cn1 >= 5 {
							for r := 0; r < len(boards[k]); r++ {
								for c := 0; c < len(boards[k][r]); c++ {
									boards[k][r][c] = -1
								}
							}
							bw++
						}
					}
				}
			}
		}
	}
	fmt.Println("bad")
}

func main() {
	part1()
	part2()
}

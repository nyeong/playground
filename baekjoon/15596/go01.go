package main

import (
	"fmt"
)

func main() {
	ns := []int{1, 2, 3, 4, 5}
	fmt.Print(sum(ns))
}

func sum(a []int) int {
	result := 0
	for _, n := range a {
		result += n
	}
	return result
}

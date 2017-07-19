package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func read() string {
	sc.Scan()
	var input = sc.Text()
	return input
}

func main() {
	input := read()
	is := make([]int, 0)
	for _, elem := range strings.Split(input, " ") {
		i, _ := strconv.Atoi(elem)
		is = append(is, i)
	}
	if is[0]%3 == 0 || is[1]%3 == 0 || (is[0]+is[1])%3 == 0 {
		fmt.Println("Possible")
	} else {
		fmt.Println("Impossible")
	}
}

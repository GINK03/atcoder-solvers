package main

import (
  "bufio"
  "fmt"
  "os"
  "sort"
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
  input := strings.Split(read(), " ")
  k, _ := strconv.Atoi(input[1])
  arr := strings.Split(read(), " ")
  iarr := make([]int, 0)
  for _, a := range arr {
    i, _ := strconv.Atoi(a)
    iarr = append(iarr, i)
  }
  sort.Ints(iarr)
  sum := 0
  for _, i := range iarr[len(iarr)-1*k:] {
    sum += i
  }
  fmt.Println(sum)
}

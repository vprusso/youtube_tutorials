// p12. Functions
package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func add3(a, b, c int) int {
    return a + b + c
}


func main() {
    ans := add(1, 1)
    fmt.Println(ans)

    ans = add3(1, 1, 1)
    fmt.Println(ans)

}

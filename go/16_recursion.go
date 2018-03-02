// p.16 Recursion

// n! = n * n-1 * n-2 * .. * 1
// 5! = 5 * 4 * 3 * 2 * 1

package main

import "fmt"

func fact(n int)int {
    if n <= 1 {
        return 1
    }
    return n * fact(n-1)
}

func main(){
    fmt.Println(fact(5))
}

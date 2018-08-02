// YouTube Video: https://www.youtube.com/watch?v=K6mJ7Ed0DIA&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
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

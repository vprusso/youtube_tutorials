// YouTube Video: https://www.youtube.com/watch?v=d2wl9hlxyeA&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
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

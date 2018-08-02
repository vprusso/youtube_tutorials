// YouTube Video: https://www.youtube.com/watch?v=roF5YIKNX1M&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p13. Multiple Return Values
package main

import "fmt"

func add_sub(a int, b int) (int, int) {
    return a+b, a-b
}

func main() {
    add_res, sub_res := add_sub(1, 1)
    fmt.Println("add_res:", add_res, "sub_res:", sub_res)

    add_res_2, _ := add_sub(2, 2)
    fmt.Println("add_res_2:", add_res_2)
}

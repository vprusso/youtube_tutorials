// YouTube Video: https://www.youtube.com/watch?v=uBbL3QsJyFk&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p2. Values
package main

//import "fmt"
//import "time"

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("hello world")
    fmt.Println("hello" + "world")

    fmt.Println(1 + 1)
    fmt.Println(1 - 1)
    fmt.Println(1 * 1)
    fmt.Println(1 % 1)

    fmt.Println("1+1 is equal to: ", 1+1)
    fmt.Println("5*5 is equal to: ", 5*5)

    fmt.Println("1.01 - 0.99=", 1.01-0.99)

    fmt.Println(true)
    fmt.Println(5 == 5)
    fmt.Println(5 == 6)

    fmt.Println("The time is: ", time.Now())

}

// YouTube Video: https://www.youtube.com/watch?v=lHJ33KvdyN4&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p4. Constants
package main

import "fmt"

func main() {
    const pi float64 = 3.1415926

    fmt.Println(pi)

    const c int = 1000

    fmt.Println(c)

    // Can't reassign value to constant.
    //c = 50 

    var d int = 100

    fmt.Println(d)

    d = 5000

    fmt.Println(d)



}

// YouTube Video: https://www.youtube.com/watch?v=MnUQoVk44n0&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.15 Closures

package main

import "fmt"

func say_hello(msg string){
    fmt.Println(msg)
}

func return_anoyn_func() func(string) {
    // return an anonymous function
    return func(msg string){
        fmt.Print(msg)
    }
}

func int_seq() func() int {
    i := 0
    return func() int {
        i++
        return i
    }
}

func main(){

    say_hello("Hello")

    // anonymous function declared:
    func(msg string){
        fmt.Println(msg)
    }("Hello Anonymous")

    //print_func := return_anoyn_func()
    //print_func("Hello returned from anonymous")

    next_int := int_seq()

    fmt.Println(next_int())
    fmt.Println(next_int())

    next_int2 := int_seq()

    fmt.Println(next_int2())

}

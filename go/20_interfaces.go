// YouTube Video: https://www.youtube.com/watch?v=EGRXKV6j-v0&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.20 Interfaces

package main

import (
    "fmt"
    "math"
)

// interface for shapes:
type geometry interface {
    area() float64
    perim() float64
}

type rect struct {
    width, height float64
}

type circle struct {
    radius float64
}

// implement all methods for interface:
func (r rect) area() float64 {
    return r.width * r.height
}

func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}

func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
    return 2 * math.Pi * c.radius
}

func measure(g geometry) {
    fmt.Println(g)
    fmt.Println(g.area())
    fmt.Println(g.perim())
}

func main(){

    r := rect{width: 5, height: 10}
    c := circle{radius: 5}

    measure(r)
    measure(c)
}

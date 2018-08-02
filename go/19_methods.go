// YouTube Video: https://www.youtube.com/watch?v=1h5e-g2vqCc&t=0s&list=PL5tcWHG-UPH0jOCtEIpDNpbwOnhc6h9Om
// p.19 Methods

package main

import "fmt"

type rect struct {
    width, height int
}

// method defined for value reciever type.
func (r rect) area() int {
    return r.width + r.height
}

// method defined for pointer reciever type.
func (r *rect) perim() int {
    return 2*r.width * 2*r.height
}

func main(){

    r := rect{width: 10, height: 5}

    // call to method for value reciever type.
    fmt.Println("area:", r.area())
    fmt.Println("perim:", r.perim())

    r_ptr := &r

    // call to method for pointer reciever type.
    fmt.Println("area:", r_ptr.area())
    fmt.Println("perim:", r_ptr.perim())

}

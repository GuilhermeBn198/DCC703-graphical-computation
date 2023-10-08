package main

import (
	"fmt"
	"strconv"
)

const size = 80

type Point struct {
    value string
    x, y, z int
}

func CreatePoint(x, y, z int) Point {
    var p Point
    p.x, p.y, p.z = x, y, z

    return p
} 

type Plane [size][size]Point

func CreatePlane() Plane {
    var p Plane

    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {
            p[i][j].value = "\033[90mO\033[39m"
        }
    }

    return p
} 

func (p *Plane) Clear() {
    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {
            p[i][j].value = "\033[90mO\033[39m"
        }
    }
}

func (p *Plane) Print(name string) {
    fmt.Println("")

    if name != "" {
        fmt.Println(name)
    }

    for i := 0; i < len(strconv.Itoa(size)) + size * 2 + 6; i++ {
        fmt.Print("-")
    }

    fmt.Println("")

    for i := 0; i < size; i++ {
        fmt.Printf("| %02d | ", size - i - 1)
        for j := 0; j < size; j++ {
            fmt.Print(p[i][j].value + " ")
        }
        fmt.Println("|")
    }

    for i := 0; i < len(strconv.Itoa(size)) + size * 2 + 6; i++ {
        fmt.Print("-")
    }

    fmt.Println("")
    fmt.Println("")
}

func (p *Plane) AnimatedPrint(name string) {
    fmt.Println("")

    if name != "" {
        fmt.Println(name)
    }

    for i := 0; i < len(strconv.Itoa(size)) + size * 2 + 6; i++ {
        fmt.Print("-")
    }

    fmt.Println("")

    for i := 0; i < size; i++ {
        fmt.Printf("| %02d | ", size - i - 1)
        for j := 0; j < size; j++ {
            fmt.Print(p[i][j].value + " ")
        }
        fmt.Println("|")
    }

    for i := 0; i < len(strconv.Itoa(size)) + size * 2 + 6; i++ {
        fmt.Print("-")
    }

    fmt.Println("")
    fmt.Println("")
}

func (p *Plane) SwitchPixel(x, y int) {
    if size - y - 1 >= size || x >= size || size - y - 1 < 0 || x < 0 {
        return
    }

    p[size - y - 1][x].value = "\033[91mX\033[39m"
}

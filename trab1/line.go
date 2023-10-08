package main

import (
	"math"
)

func Analytic(p Plane, p1, p2 Point) {
    p.Clear()

    if p1.x == p2.x {
       for y := p1.y; y <= p2.y; y++ {
            p.SwitchPixel(p1.x, y)
       } 

        p.Print("Algoritmo: Método Analítico")

        return
    }

    m := float64((p2.y - p1.y))  / float64((p2.x - p1.x))
    b := float64(p2.y) - m * float64(p2.x)

    for x := p1.x; x <= p2.x; x++ {
        y := m * float64(x)  + b

        p.SwitchPixel(x, int(y + 0.5))
    }

    p.Print("Algoritmo: Método Analítico")
}

func DDA(p Plane, p1, p2 Point) {
    p.Clear()

    if math.Abs(float64(p2.x - p1.x)) > math.Abs(float64(p2.y - p1.y)) {
        inc := float64((p2.y - p1.y)) / float64((p2.x - p1.x))
        var y float64 = float64(p1.y)

       for x := p1.x; x <= p2.x; x++ {
            p.SwitchPixel(x, int(y + 0.5))
            y = y + inc
       } 
    } else {
        inc := float64((p2.x - p1.x)) / float64((p2.y - p1.y))
        var x float64 = float64(p1.x)

       for y := p1.y; y <= p2.y; y++ {
            p.SwitchPixel(int(x + 0.5), y)
            x = x + inc
       } 
    }

    p.Print("Algoritmo: DDA")
}

func BresenhamLine(p Plane, p1, p2 Point) {
    p.Clear()

    dx := p2.x - p1.x

    if dx < 0 {
        dx = -dx
    }

    dy := p2.y - p1.y

    if dy > 0 {
        dy = -dy
    }

    sy := 1

    if p1.y >= p2.y {
        sy = -1
    }

    slope := dx + dy

    x := p1.x
    y := p1.y

    for {
        p.SwitchPixel(x, y)

        if x == p2.x && y == p2.y {
            break
        }

        eslope := 2 * slope

        if eslope >= dy {
            if x == p2.x {
                break
            }

            slope = slope + dy
            x++
        }

        if eslope <= dx {
            if y == p2.y {
                break
            }

            slope = slope + dx
            y = y + sy
        }
    }

    p.Print("Algoritmo: Bresenham")
}

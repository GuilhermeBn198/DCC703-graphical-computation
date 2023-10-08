package main

import (
	"math"
)

func Parametric(p Plane, p1 Point, r int) {
    p.Clear()

    x := float64(p1.x + r)
    y := float64(p1.y)
    var i float64
    
    for i = 1; i <= 360; i++ {
        p.SwitchPixel(int(x + 0.5), int(y + 0.5))
        
        x = float64(p1.x) + float64(r) * math.Cos(math.Pi * i / 180.0)
        y = float64(p1.y) + float64(r) * math.Sin(math.Pi * i / 180.0)
    }

    p.Print("Algoritmo: Equação Paramétrica")
}

func SymmetricalIncrement(p Plane, p1 Point, r int) {
    p.Clear()

    th := 0.0
    dth := 1.0 / float64(r)
    x := float64(r)
    y := 0.0
    
    for th <= math.Pi / 4.0 {
        p.SwitchPixel(int(float64(p1.x) + x + 0.5), int(float64(p1.y) + y + 0.5))
        p.SwitchPixel(int(float64(p1.x) + x + 0.5), int(float64(p1.y) - y + 0.5))
        p.SwitchPixel(int(float64(p1.x) - x + 0.5), int(float64(p1.y) + y + 0.5))
        p.SwitchPixel(int(float64(p1.x) - x + 0.5), int(float64(p1.y) - y + 0.5))
        p.SwitchPixel(int(float64(p1.x) + y + 0.5), int(float64(p1.y) + x + 0.5))
        p.SwitchPixel(int(float64(p1.x) + y + 0.5), int(float64(p1.y) - x + 0.5))
        p.SwitchPixel(int(float64(p1.x) - y + 0.5), int(float64(p1.y) + x + 0.5))
        p.SwitchPixel(int(float64(p1.x) - y + 0.5), int(float64(p1.y) - x + 0.5))
        
        th = th + dth
        x = x - y * dth
        y = y + x * dth
    }

    p.Print("Algoritmo: Incremental com Simetria")
}

func BresenhamCircle(p Plane, p1 Point, r int) {
    p.Clear()

    x := 0
    y := r
    pp := 3 - 2 * r
    
    p.SwitchPixel(p1.x + x, p1.y + y)
    p.SwitchPixel(p1.x + x, p1.y - y)
    p.SwitchPixel(p1.x - x, p1.y + y)
    p.SwitchPixel(p1.x - x, p1.y - y)
    p.SwitchPixel(p1.x + y, p1.y + x)
    p.SwitchPixel(p1.x + y, p1.y - x)
    p.SwitchPixel(p1.x - y, p1.y + x)
    p.SwitchPixel(p1.x - y, p1.y - x)
    
    for x <= y {
        x++

        if pp > 0 {
            y--
            pp = pp + 4 * (x - y) + 10
        } else {
            pp = pp + 4 * x + 6
        }

        p.SwitchPixel(p1.x + x, p1.y + y)
        p.SwitchPixel(p1.x + x, p1.y - y)
        p.SwitchPixel(p1.x - x, p1.y + y)
        p.SwitchPixel(p1.x - x, p1.y - y)
        p.SwitchPixel(p1.x + y, p1.y + x)
        p.SwitchPixel(p1.x + y, p1.y - x)
        p.SwitchPixel(p1.x - y, p1.y + x)
        p.SwitchPixel(p1.x - y, p1.y - x)
    }

    p.Print("Algoritmo: Bresenham")
}

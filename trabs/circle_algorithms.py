import math

def parametric(plane, p1, r):
    plane.clear()

    x = p1.x + r
    y = p1.y

    for i in range(1, 361):
        plane.switch_pixel(int(x + 0.5), int(y + 0.5))
        x = p1.x + r * math.cos(math.pi * i / 180.0)
        y = p1.y + r * math.sin(math.pi * i / 180.0)

    plane.print("Algoritmo: Equação Paramétrica")

def symmetrical_increment(plane, p1, r):
    plane.clear()

    th = 0.0
    dth = 1.0 / r
    x = r
    y = 0.0
    while th <= math.pi / 4.0:
        # Switch eight pixels symmetrically around the circle
        plane.switch_pixel(int(p1.x + x + 0.5), int(p1.y + y + 0.5))
        plane.switch_pixel(int(p1.x + x + 0.5), int(p1.y - y + 0.5))
        plane.switch_pixel(int(p1.x - x + 0.5), int(p1.y + y + 0.5))
        plane.switch_pixel(int(p1.x - x + 0.5), int(p1.y - y + 0.5))
        plane.switch_pixel(int(p1.x + y + 0.5), int(p1.y + x + 0.5))
        plane.switch_pixel(int(p1.x + y + 0.5), int(p1.y - x + 0.5))
        plane.switch_pixel(int(p1.x - y + 0.5), int(p1.y + x + 0.5))
        plane.switch_pixel(int(p1.x - y + 0.5), int(p1.y - x + 0.5))

        th = th + dth
        x = x - y * dth
        y = y + x * dth

    plane.print("Algoritmo: Incremental com Simetria")

def bresenham_circle(plane, p1, r):
    plane.clear()

    x = 0
    y = r
    pp = 1 - r

    # Switch eight pixels symmetrically around the circle
    plane.switch_pixel(p1.x + x, p1.y + y)
    plane.switch_pixel(p1.x + x, p1.y - y)
    plane.switch_pixel(p1.x - x, p1.y + y)
    plane.switch_pixel(p1.x - x, p1.y - y)
    plane.switch_pixel(p1.x + y, p1.y + x)
    plane.switch_pixel(p1.x + y, p1.y - x)
    plane.switch_pixel(p1.x - y, p1.y + x)
    plane.switch_pixel(p1.x - y, p1.y - x)

    while x <= y:

        if pp > 0:
            y -= 1
            pp = pp + 2 * (x - y) + 5
        else:
            pp = pp + 2 * x + 3

        x += 1
        # Switch eight pixels symmetrically around the circle
        plane.switch_pixel(p1.x + x, p1.y + y)
        plane.switch_pixel(p1.x + x, p1.y - y)
        plane.switch_pixel(p1.x - x, p1.y + y)
        plane.switch_pixel(p1.x - x, p1.y - y)
        plane.switch_pixel(p1.x + y, p1.y + x)
        plane.switch_pixel(p1.x + y, p1.y - x)
        plane.switch_pixel(p1.x - y, p1.y + x)
        plane.switch_pixel(p1.x - y, p1.y - x)

    plane.print("Algoritmo: Bresenham")

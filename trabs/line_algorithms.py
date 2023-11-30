import math

def analytic(plane, p1, p2):
    plane.clear()
    if p1.x == p2.x:
        for y in range(p1.y, p2.y + 1):
            plane.switch_pixel(p1.x, y)
        plane.print("Algoritmo: Método Analítico")
        return

    m = (p2.y - p1.y) / (p2.x - p1.x)
    b = p2.y - m * p2.x

    for x in range(p1.x, p2.x + 1):
        y = m * x + b
        plane.switch_pixel(x, int(y + 0.5))

    # plane.print("Algoritmo: analitico")

def analyticRemember(plane, p1, p2):
    if p1.x == p2.x:
        for y in range(p1.y, p2.y + 1):
            plane.switch_pixel(p1.x, y)
        plane.print("Algoritmo: Método Analítico")
        return

    m = (p2.y - p1.y) / (p2.x - p1.x)
    b = p2.y - m * p2.x

    for x in range(p1.x, p2.x + 1):
        y = m * x + b
        plane.switch_pixel(x, int(y + 0.5))

    # plane.print("Algoritmo: analitico")

###################################################

def dda(plane, p1, p2):
    plane.clear()
    if abs(p2.x - p1.x) > abs(p2.y - p1.y):
        inc = (p2.y - p1.y) / (p2.x - p1.x)
        y = p1.y

        for x in range(p1.x, p2.x + 1):
            plane.switch_pixel(x, int(y + 0.5))
            y = y + inc
    else:
        inc = (p2.x - p1.x) / (p2.y - p1.y)
        x = p1.x

        for y in range(p1.y, p2.y + 1):
            plane.switch_pixel(int(x + 0.5), y)
            x = x + inc

    # plane.print("Algoritmo: DDA")

def ddaRemember(plane, p1, p2):
    if abs(p2.x - p1.x) > abs(p2.y - p1.y):
        inc = (p2.y - p1.y) / (p2.x - p1.x)
        y = p1.y

        for x in range(p1.x, p2.x + 1):
            plane.switch_pixel(x, int(y + 0.5))
            y = y + inc
    else:
        inc = (p2.x - p1.x) / (p2.y - p1.y)
        x = p1.x

        for y in range(p1.y, p2.y + 1):
            plane.switch_pixel(int(x + 0.5), y)
            x = x + inc

# plane.print("Algoritmo: DDA")

################################################################

def bresenham_line(plane, p1, p2):
    plane.clear()
    dx = abs(p2.x - p1.x)
    dy = abs(p2.y - p1.y) * -1
    sy = 1 if p1.y < p2.y else -1
    slope = dx + dy
    x, y = p1.x, p1.y

    while True:
        plane.switch_pixel(x, y)

        if x == p2.x and y == p2.y:
            break

        eslope = 2 * slope

        if eslope >= dy:
            if x == p2.x:
                break
            slope += dy
            x += 1

        if eslope <= dx:
            if y == p2.y:
                break
            slope += dx
            y += sy

        if x > p2.x or y > p2.y:
            break

    # plane.print("Algoritmo: Bresenham")

def bresenham_lineRemember(plane, p1, p2):
    dx = abs(p2.x - p1.x)
    dy = abs(p2.y - p1.y) * -1
    sy = 1 if p1.y < p2.y else -1
    if p1.x < p2.x:
        sx = 1
    else:
        sx = -1
    slope = dx + dy
    x, y = p1.x, p1.y

    while True:
        plane.switch_pixel_color(x, y, "\033[92mX\033[92m")

        if x == p2.x and y == p2.y:
            break

        eslope = 2 * slope

        if eslope >= dy:
            if x == p2.x:
                break
            slope += dy
            x += sx

        if eslope <= dx:
            if y == p2.y:
                break
            slope += dx
            y += sy

    # plane.print("Algoritmo: Bresenham")
    
def bresenham_lineRemember_clip(plane, p1, p2):
    dx = abs(p2.x - p1.x)
    dy = abs(p2.y - p1.y) * -1
    sy = 1 if p1.y < p2.y else -1
    if p1.x < p2.x:
        sx = 1
    else:
        sx = -1
    slope = dx + dy
    x, y = p1.x, p1.y

    while True:
        plane.switch_pixel_color(x, y, "\033[93mX\033[93m")

        if x == p2.x and y == p2.y:
            break

        eslope = 2 * slope

        if eslope >= dy:
            if x == p2.x:
                break
            slope += dy
            x += sx

        if eslope <= dx:
            if y == p2.y:
                break
            slope += dx
            y += sy

    # plane.print("Algoritmo: Bresenham")
import math
from point import Point
import numpy as np

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

def casteljau(points, plane):
    casteljauRecursive(points, 12, plane)

def casteljauRecursive(points, deep, plane):
    if deep <= 0:
        return
    m = [
        Point((points[0].x + points[1].x)/2, (points[0].y + points[1].y)/2, 0),
        Point((points[1].x + points[2].x)/2, (points[1].y + points[2].y)/2, 0),
        Point((points[2].x + points[3].x)/2, (points[2].y + points[3].y)/2, 0)
    ]
    m.append(Point((m[0].x + m[1].x)/2, (m[0].y + m[1].y)/2, 0))
    m.append(Point((m[1].x + m[2].x)/2, (m[1].y + m[2].y)/2, 0))
    m.append(Point((m[3].x + m[4].x)/2, (m[3].y + m[4].y)/2, 0))

    plane.switch_pixel(int(m[5].x + 0.5), int(m[5].y + 0.5))

    casteljauRecursive([points[0], m[0], m[3], m[5]], deep - 1, plane)
    casteljauRecursive([m[5], m[4], m[2], points[3]], deep - 1, plane)

def bezier_curve_parametric(plane, points):
    increment = 0.0005
    for t in np.arange(0, 1, increment):
        x = (1 - t)**3 * points[0].x + 3 * t * (1 - t)**2 * points[1].x + 3 * t**2 * (1 - t) * points[2].x + t**3 * points[3].x
        y = (1 - t)**3 * points[0].y + 3 * t * (1 - t)**2 * points[1].y + 3 * t**2 * (1 - t) * points[2].y + t**3 * points[3].y
        plane.switch_pixel(int(x + 0.5), int(y + 0.5))
        
from point import Point
from line_algorithms import bresenham_lineRemember_clip, bresenham_lineRemember


def inside(p, cp1, cp2):
    return (cp2.x - cp1.x) * (p.y - cp1.y) >= (cp2.y - cp1.y) * (p.x - cp1.x)

def computeIntersection(cp1, cp2, s, e):
    dc = [cp1.x - cp2.x, cp1.y - cp2.y]
    dp = [s.x - e.x, s.y - e.y]
    n1 = cp1.x * cp2.y - cp1.y * cp2.x
    n2 = s.x * e.y - s.y * e.x
    n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
    return Point((n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3)

def clip(subjectPolygon, clipPolygon, plane):
    outputList = subjectPolygon

    # For each edge in clipPolygon
    for i in range(len(clipPolygon)):
        inputList = outputList
        outputList = []

        # Get clip edge
        cp1 = clipPolygon[i]
        cp2 = clipPolygon[(i+1)%len(clipPolygon)]

        # For each edge in the subject polygon
        for j in range(len(inputList)):
            s = inputList[j]
            e = inputList[(j+1)%len(inputList)]

            # Case 1: Both vertices are inside:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    outputList.append(computeIntersection(cp1, cp2, s, e))
                outputList.append(e)
            # Case 2: Only the first vertex is inside
            elif inside(s, cp1, cp2):
                outputList.append(computeIntersection(cp1, cp2, s, e))

    # Draw the points of the subject polygon
    for point in subjectPolygon:
        print(f"Subject Polygon Point: {point.x}, {point.y}")
        plane.switch_pixel_color(point.x, point.y, "\033[93m1\033[93m")

    # Draw the points of the clip polygon
    for point in clipPolygon:
        print(f"Clip Polygon Point: {point.x}, {point.y}")
        plane.switch_pixel_color(point.x, point.y, "\033[92m2\033[92m")

    # Draw the points of the output list (clipped points)
    for point in outputList:
        print(f"Clipped Point: {point.x}, {point.y}")
        plane.switch_pixel_color(point.x, point.y, "\033[92mC\033[92m")
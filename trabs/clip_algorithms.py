from point import Point
from line_algorithms import bresenham_lineRemember_clip, bresenham_lineRemember

def clip(subjectPolygon, clipPolygon, plane):
    def inside(p, cp1, cp2):
        return (cp2.x - cp1.x) * (p.y - cp1.y) > (cp2.y - cp1.y) * (p.x - cp1.x)

    def computeIntersection(cp1, cp2, s, e):
        dc = [cp1.x - cp2.x, cp1.y - cp2.y]
        dp = [s.x - e.x, s.y - e.y]
        n1 = cp1.x * cp2.y - cp1.y * cp2.x
        n2 = s.x * e.y - s.y * e.x
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return Point((n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3)

    def clipSide(cp1, cp2, inputList):
        outputList = []
        if inputList:
            s = inputList[-1]
            for e in inputList:
                if inside(e, cp1, cp2):
                    if not inside(s, cp1, cp2):
                        intersection = computeIntersection(cp1, cp2, s, e)
                        outputList.append(intersection)
                        plane.switch_pixel_color(intersection.x, intersection.y, "\033[94mX\033[94m")  
                        
                    outputList.append(e)
                elif inside(s, cp1, cp2):
                    intersection = computeIntersection(cp1, cp2, s, e)
                    outputList.append(intersection)
                    plane.switch_pixel_color(intersection.x, intersection.y, "\033[94mX\033[94m")  
                    
                s = e
        return outputList

    outputList = subjectPolygon
    for i in range(len(clipPolygon)):
        cp1 = clipPolygon[i]
        cp2 = clipPolygon[(i+1) % len(clipPolygon)]
        outputList = clipSide(cp1, cp2, outputList)

    for i in range(len(outputList)):
        point1 = outputList[i]
        point2 = outputList[(i+1) % len(outputList)]
        bresenham_lineRemember(plane, point1, point2)
def onBoundary(px, py, x1, y1, x2, y2):
    if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
        return (x2 - x1) * (py - y1) == (px - x1) * (y2 - y1)
    return False

def insidePoligon(n, polygon, m, puncte):
    rezultate = []

    for px,py in points:
        on_boundary = False
        intersectii = 0

        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]

            if onBoundary(px, py, x1, y1, x2, y2):
                on_boundary = True
                break

            if (y1 > py) != (y2 > py):
                x_intersectie = x1+(py-y1)*(x2-x1)/(y2-y1)
                if px < x_intersectie:
                    intersectii += 1

        if on_boundary:
            rezultate.append("BOUNDARY")
        elif intersectii % 2 == 1:
            rezultate.append("INSIDE")
        else:
            rezultate.append("OUTSIDE")

    return rezultate

n = int(input())
polygon = []
for i in range(n):
    x,y = map(int,input().split())
    polygon.append((x,y))
m = int(input())
points = []
for i in range(m):
    x,y = map(int,input().split())
    points.append((x,y))

for rezultat in insidePoligon(n, polygon, m, points):
    print(rezultat)
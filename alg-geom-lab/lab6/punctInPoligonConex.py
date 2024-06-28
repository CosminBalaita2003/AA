def orientare (a,b,c):
    val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if val == 0:
        return 0 # coliniare
    if val > 0:
        return 1 # clockwise
    return 2 # counterclockwise

def peSegment(a,b,c):
    if (b[0] <= max(a[0], c[0]) and b[0] >= min(a[0], c[0]) and b[1] <= max(a[1], c[1]) and b[1] >= min(a[1], c[1])):
        return True
    return False

def punctInPoligon(polygon, punct):
    n = len(polygon)
    if n < 3:
        return "OUTSIDE"
    
    #cautare binara pentru a gasi cele 2 puncte si punctul de referinta
    l=1
    r=n-1
    while r-l>1:
        m=(l+r)//2
        if orientare(polygon[0],polygon[m],punct)==2:
            l=m
        else:
            r=m

    inInterior = orientare(polygon[0],polygon[l],punct) ==  2 and orientare(polygon[l],polygon[r],punct) == 2 and orientare(polygon[r],polygon[0],punct) == 2
    if inInterior:
        return "INSIDE"
    
    if orientare(polygon[0],polygon[l],punct) == 0 and peSegment(polygon[0], punct ,polygon[l]) :
        return "BOUNDARY"
    if orientare(polygon[l],polygon[r],punct) == 0 and peSegment(polygon[l], punct, polygon[r]) :
        return "BOUNDARY"
    if orientare(polygon[r],polygon[0],punct) == 0 and peSegment(polygon[r], punct, polygon[0]) :
        return "BOUNDARY"
    
    return "OUTSIDE"

n=int(input())
polygon = []
for i in range(n):
    x,y = map(int,input().split())
    polygon.append((x,y))
m=int(input())
puncte = []
for i in range(m):
    x,y = map(int,input().split())
    puncte.append((x,y))


for punct in puncte:
    print(punctInPoligon(polygon, punct))

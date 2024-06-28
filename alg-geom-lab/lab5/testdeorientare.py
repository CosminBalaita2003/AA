#Graham scan
n = int(input())
puncte = []
for i in range(n):
    x,y = map(int,input().split())
    puncte.append((x,y))

def viraj(xP, yP, xQ, yQ, xR, yR):
    return xQ*yR + xP*yQ + xR*yP - xQ*yP - xP*yR - xR*yQ

start = puncte[0]
for i in range(n):
    if puncte[i][0] < start[0]:
        start = puncte[i]
    elif puncte[i][0] == start[0] and puncte[i][1] < start[1]:
        start = puncte[i]

p1 = puncte.index(start)
p2 = (p1 + 1) % n
poligon = [puncte[p1], puncte[p2]]

for i in range(p2, n):
    poligon.append(puncte[i])
    while len(poligon) > 2 and viraj(poligon[-3][0], poligon[-3][1], poligon[-2][0], poligon[-2][1], poligon[-1][0], poligon[-1][1]) <= 0:
        poligon.pop(-2)

for i in range(0, p1 + 1):
    poligon.append(puncte[i])
    while len(poligon) > 2 and viraj(poligon[-3][0], poligon[-3][1], poligon[-2][0], poligon[-2][1], poligon[-1][0], poligon[-1][1]) <= 0:
        poligon.pop(-2)

poligon.pop(-1)

k = len(poligon)
print(str(k))
for i in range(k):
    print(str(poligon[i][0]) + " " + str(poligon[i][1]))
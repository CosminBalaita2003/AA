def e_monoton (n, poligon, axis):
    if axis == 'x': 
        index=0 
    else:
        index=1

    min_index = min(range(n), key=lambda i: poligon[i][index])
    max_index = max(range(n), key=lambda i: poligon[i][index])
    
    
    coor_curenta = poligon[min_index][index]
    i=min_index
    while i!=max_index: #verificam daca poligonul este monoton crescator
        next_index = (i+1)%n
        if poligon[next_index][index] < coor_curenta: #daca gasim un punct mai mic decat cel curent, poligonul nu este monoton
            break
        coor_curenta = poligon[next_index][index]
        i = next_index
    else:  
        coor_curenta = poligon[max_index][index] 
        i=max_index
        while i!=min_index:
            next_index = (i+1)%n
            if poligon[next_index][index] > coor_curenta:
                return False
            coor_curenta = poligon[next_index][index]
            i = next_index
        return True
    
    coor_curenta = poligon[min_index][index]
    i=min_index
    while i!=max_index: #verificam daca poligonul este monoton descrescator
        next_index = (i+1)%n
        if poligon[next_index][index] > coor_curenta:
            return False
        coor_curenta = poligon[next_index][index]
        i = next_index
    return True

# file=open("input.in","r")
# n=int(file.readline())
# poligon = []
# for i in range(n):
#     x,y = map(int,file.readline().split())
#     poligon.append((x,y))

n=int(input())
poligon = []
for i in range(n):
    x,y = map(int,input().split())
    poligon.append((x,y))


x_monoton = e_monoton(n, poligon, 'x')
y_monoton = e_monoton(n, poligon, 'y')

print("YES" if x_monoton else "NO")
print("YES" if y_monoton else "NO")
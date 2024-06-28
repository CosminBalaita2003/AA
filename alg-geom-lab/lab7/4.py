def intersectie(semiplane, punct):
    max_x, max_y = 9999999999, 9999999999
    min_x, min_y = -9999999999, -9999999999

    for s in semiplane:

        a,b,c = s
        if a == 0:  # este semiplan vertical
            if (c+ b * punct[1] ) >= 0:
                continue
        else:  # este semiplan orizontal
            if (c + a * punct[0] ) >= 0:
                continue

        if a == 0:  # este semiplan vertical
            if -1 * c / b < punct[1]:
                min_y = max(min_y, -1 * c / b)
            else:
                max_y = min(max_y, -1 * c / b)
        else:  # este semiplan orizontal
            if -1 * c / a < punct[0]:
                min_x = max(min_x, -1 * c / a)
            else:
                max_x = min(max_x, -1 * c / a)

    if  max(max_x, max_y) == 9999999999 or min(min_x, min_y) == -9999999999 :
        return 0 # nu exista 
    return (max_x - min_x) * (max_y - min_y) # aria dreptunghiului

semiplane = []
n = int(input())
for i in range (n):
    a,b,c = map(float, input().split())
    semiplane.append((a,b,c))

puncte = []
m = int(input())
for i in range(m):
    x,y = map(float, input().split())
    puncte.append((x,y))

results = []
for punct in puncte:
    results.append(intersectie(semiplane, punct))

for res in results:
    if res == 0:
        print("NO")
    else:
        print("YES")
        print("{:.6f}".format(res))
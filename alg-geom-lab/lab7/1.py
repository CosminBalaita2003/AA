

def determinant(matrix):
    a, b, c, d = matrix[0]
    e, f, g, h = matrix[1]
    i, j, k, l = matrix[2]
    m, n, o, p = matrix[3]
    
    det = (
        a * (f * (k * p - o * l) - g * (j * p - n * l) + h * (j * o - n * k)) -
        b * (e * (k * p - o * l) - g * (i * p - m * l) + h * (i * o - m * k)) +
        c * (e * (j * p - n * l) - f * (i * p - m * l) + h * (i * n - m * j)) -
        d * (e * (j * o - n * k) - f * (i * o - m * k) + g * (i * n - m * j))
    )
    return det

def classify_point(xA, yA, xB, yB, xC, yC, x, y):
    matrix = [
        [xA, yA, xA**2 + yA**2, 1],
        [xB, yB, xB**2 + yB**2, 1],
        [xC, yC, xC**2 + yC**2, 1],
        [x, y, x**2 + y**2, 1]
    ]
    det = determinant(matrix)
    if det > 0:
        return "INSIDE"
    elif det == 0:
        return "BOUNDARY"
    else:
        return "OUTSIDE"



xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
results = []
for x, y in points:
    result = classify_point(xA, yA, xB, yB, xC, yC, x, y)
    results.append(result)

for result in results:
    print(result)

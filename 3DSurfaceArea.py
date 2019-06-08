def findArea(i, j):
    master = surface[i][j]
    up = master - surface[i-1][j]
    down = master - surface[i+1][j]
    left = master - surface[i][j-1]
    right = master - surface[i][j+1]
    count = 2
    count += up if up > 0 else 0
    count += down if down > 0 else 0
    count += left if left > 0 else 0
    count += right if right > 0 else 0
    return count

def generateSurface(surface, h, w):
    for row in surface:
        row.insert(0, 0)
        row.append(0)
    boundary = [0 for i in range(w + 2)]
    surface.insert(0, boundary)
    surface.append(boundary)

parameters = [int(i) for i in input().split()]
h = parameters[0]
w = parameters[1]

surface = []
for row in range(h):
    surface.append([int(i) for i in input().split()])

generateSurface(surface, h, w)

total = 0
for i in range(1, h+1):
    for j in range(1, w+1):
        sides = findArea(i ,j)
        total += sides

print(total)
def checkCavity(i, j):
    main = map[i][j]
    top = map[i-1][j]
    bottom = map[i+1][j]
    left = map[i][j-1]
    right = map[i][j+1]
    if (main > top) and (main > bottom) and (main > left) and (main > right):
        return True
    return False

n = int(input())
map = []
for i in range(n):
    map.append(list(input()))

cavities = []
for i in range(1, n-1):
    for j in range(1, n-1):
        if checkCavity(i, j):
            cavities.append([i, j])

for cavity in cavities:
    map[cavity[0]][cavity[1]] = 'X'

for i in map:
    for j in i:
        print(j, end='')
    print()
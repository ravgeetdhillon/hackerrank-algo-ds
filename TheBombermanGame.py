def destroy(spot):
    i = spot[0]
    j = spot[1]
    grid[i][j] = '.'
    if i - 1 >= 0:
        grid[i - 1][j] = '.'
    if i + 1 < r:
        grid[i + 1][j] = '.'
    if j - 1 >= 0:
        grid[i][j - 1] = '.'
    if j + 1 < c:
        grid[i][j + 1] = '.'

def display(grid):
    for i in range(r):
        for j in range(c):
            print( grid[i][j], end='' )
        print()

parameters = [int(i) for i in input().split()]
r = parameters[0]
c = parameters[1]
time = parameters[2]

grid = []
for _ in range(r):
    grid.append( list(input()) )

stack = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'O':
            stack.append([i, j])

if time > 1:
    time = time % 4
    if time != 3:
        time += 4

for sec in range(2, time + 1):
    if sec % 2 == 0:
        for i in range(r):
            for j in range(c):
                grid[i][j] = 'O'
    elif sec % 2 == 1:
        while len(stack) > 0:
            spot = stack.pop()
            destroy(spot)
        stack = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    stack.append([i, j])
display(grid)
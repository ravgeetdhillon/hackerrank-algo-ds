tests = int( input() )
for _ in range(tests):
    n = int( input() )
    grid = []
    for i in range(n):
        grid.append( [int(i) for i in input().split() ] )

    container = {}
    for row in grid:
        sum = 0
        for cell in row:
            sum += cell
        if sum in container:
            container[sum] += 1
        else:
            container[sum] = 1

    balls = {}
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += grid[i][j]
        if sum in balls:
            balls[sum] += 1
        else:
            balls[sum] = 1

    if container == balls:
        print("Possible")
    else:
        print("Impossible")
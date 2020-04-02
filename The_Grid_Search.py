def searchGrid(grid, pattern):
    for i in range(0, rg - rp + 1):
        for j in range(0, cg - cp + 1):
            temp = []
            for row in grid[i : i + rp]:
                temp.append(row[j : j + cp])
                if temp != pattern[:len(temp)]:
                    break
            if temp == pattern:
                return "YES"
    return "NO"

tests = int(input())
for _ in range(tests):
    parameters = [int(i) for i in input().split()]
    rg = parameters[0]
    cg = parameters[1]

    grid = []
    for i in range(rg):
        grid.append( list(input()) )

    parameters = [int(i) for i in input().split()]
    rp = parameters[0]
    cp = parameters[1]

    pattern = []
    for i in range(rp):
        pattern.append( list(input()) )

    print(searchGrid(grid, pattern))
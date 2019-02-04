def totalAttackPositions(obs, queen):
    count = 0

    #down-left
    x = queen[0]
    y = queen[1]
    while x > 1 and y > 1:
        x -= 1
        y -= 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #up-right
    x = queen[0]
    y = queen[1]
    while x < size and y < size:
        x += 1
        y += 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #up
    x = queen[0]
    y = queen[1]
    while x < size:
        x += 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #down
    x = queen[0]
    y = queen[1]
    while x > 1:
        x -= 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #up-left
    x = queen[0]
    y = queen[1]
    while x < size and y > 1:
        x += 1
        y -= 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #down-right
    x = queen[0]
    y = queen[1]
    while x > 1 and y < size:
        x -= 1
        y += 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #left
    x = queen[0]
    y = queen[1]
    while y > 1:
        y -= 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1

    #right
    x = queen[0]
    y = queen[1]
    while y < size:
        y += 1
        if [x, y] in obs:
            obs.remove([x, y])
            break
        else:
            count += 1
    return count

variables = [int(i) for i in input().split()]
queen = [int(i) for i in input().split()]

size = variables[0]
totalObstacles = variables[1]

obstacles = []
for i in range(totalObstacles):
    obstacles.append([int(i) for i in input().split()])

print(totalAttackPositions(obstacles, queen))


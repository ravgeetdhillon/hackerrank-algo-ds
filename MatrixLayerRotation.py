def displayMatrix(arr):
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=' ')
        print('')

def rotateMatrix(matrix, turns):
    for k in range(min(r, c) // 2):
        turns_temp = turns % (2 * (r + c - 2 - (4 * k)))
        for _ in range(turns_temp):
            save = matrix[k][k]
            
            #down
            for i in range(k, r-1-k):
                temp = matrix[i+1][k]
                matrix[i+1][k] = save
                save = temp

            #right
            for j in range(k, c-1-k):
                temp = matrix[r-1-k][j+1]
                matrix[r-1-k][j+1] = save
                save = temp

            #up
            for i in range(r-1-k, k, -1):
                temp = matrix[i-1][c-1-k]
                matrix[i-1][c-1-k] = save
                save = temp

            #left
            for j in range(c-1-k, k, -1):
                temp = matrix[k][j-1]
                matrix[k][j-1] = save
                save = temp
    return matrix

parameters = [int(i) for i in input().split()]
r = parameters[0]
c = parameters[1]
turns = parameters[2]
matrix = []

for _ in range(r):
    matrix.append( [int(i) for i in input().split()] )

displayMatrix( rotateMatrix(matrix, turns) )
a = input()
b = input()

def lcs(s1, s2):
    m = len(s1)

    grid = []
    for i in range(2):
        grid.append( [0 for i in range( m + 1 )] )

    for i in range(m):
        for j in range(m):
            if s1[i] == s2[j]:
                grid[1][j + 1] = grid[0][j] + 1
            else:
                grid[1][j + 1] = max( grid[1][j], grid[0][j + 1] )
        del grid[0]
        grid.append( [0 for _ in range( m + 1 )] )
    
    return grid[0][-1]

print( lcs(a, b) )
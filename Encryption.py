import math

string = input()

size = len(string)
r = math.floor( math.sqrt(size) )
c = r
while r * c < size:
    if (r < c):
        r += 1
    else:
        c += 1

grid = []
i = 0
while i < size:
    grid.append( string[i : i + c] )
    i += c

encrypted = []
for i in range(0, c):
    block = ''
    for j in range(0, r):
        try:
            block += grid[j][i]
        except:
            break
    encrypted.append(block)

print( ' '.join(encrypted) )
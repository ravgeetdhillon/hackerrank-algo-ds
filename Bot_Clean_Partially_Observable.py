import random
moves=['UP','DOWN','LEFT','RIGHT']

bot=[int(i) for i in input().split()]
matrix=[]
for i in range(5):
    matrix.append(list(input()))

cls_dist=10
for i in range(0,5):
    for j in range(0,5):
        if matrix[i][j]=='o':
            continue
        elif matrix[i][j]=='d':
             dist=abs(i-bot[0])+abs(j-bot[1])
             if dist<cls_dist:
                 cls_dist=dist
                 cls_cell=[i,j]
try:
    diff=[cls_cell[0]-bot[0],cls_cell[1]-bot[1]]
    if diff[0]==0 and diff[1]==0:
        print('CLEAN')
    elif diff[0]<0:
        print('UP')
    elif diff[0]>0:
        print('DOWN')
    elif diff[1]<0:
        print('LEFT')
    elif diff[1]>0:
        print('RIGHT')
except NameError:
    print(random.choice(moves))

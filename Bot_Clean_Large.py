bot=[int(i) for i in input().split()]
dimensions=[int(i) for i in input().split()]
matrix=[]
for i in range(dimensions[0]):
    matrix.append(list(input()))

cls_dist=dimensions[0]*dimensions[1]
for i in range(0,dimensions[0]):
    for j in range(0,dimensions[1]):
        if matrix[i][j]=='d':
             dist=abs(i-bot[0])+abs(j-bot[1])
             if dist<cls_dist:
                 cls_dist=dist
                 cls_cell=[i,j]
             
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

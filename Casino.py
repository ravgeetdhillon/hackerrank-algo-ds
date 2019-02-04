variables=[int(i) for i in input().split(',')]
m=variables[0]
n=variables[1]

matrix=[]
for i in range(m):
    matrix.append([])
    
for i in range(n):
    queue=[int(i) for i in input().split(',')]
    n=0
    for i in queue:
        matrix[n].append(i)
        n+=1

num=''
while len(num)!=m*n:
    max=-1
    for i in range(m):
        try:
            if matrix[i][-1]>max:
                max=matrix[i][-1]
                d=i
        except IndexError:
            continue
    del matrix[d][-1]
    num+=str(max)
    print(num)

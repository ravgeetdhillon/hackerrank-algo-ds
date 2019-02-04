variables=[int(i) for i in input().split()]
m=variables[0]
n=variables[1]
matrix=[]
for i in range(m):
    matrix.append(list(input()))
    
colors=['V','I','B','G','Y','O','R']

def AllClear(a,b):
    if m>a>=0 and n>b>=0:
        return 1

def ForTwo(i,j):
    if matrix[i][j] in colors:
        surround=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        for node in surround:
            try:
                if AllClear(node[0],node[1])==1:
                    if matrix[node[0]][node[1]]==matrix[i][j]:
                        return 1
            except IndexError:
                continue
for i in range(m):
    done=0
    for j in range(n):
        if ForTwo(i,j)==1:
            print(i,j)
            done=1
            break
    if done==1:
        break

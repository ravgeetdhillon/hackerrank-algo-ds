matrix=[['#','#','#','#','#','#'],
        ['#','-','#','-','-','#'],
        ['#','-','#','#','-','#'],
        ['#','-','-','-','#','#'],
        ['#','-','#','-','-','e'],
        ['#','#','#','#','#','#']]

bot=[1,1]
for i in range(6):
    for j in range(6):
        if matrix[i][j]=='e':
            escape=[i,j]
            break

queue=[bot]
origin=[[-1,-1]]
n=0

while escape not in queue:
    cur_pos=queue[n]
    surround=[[cur_pos[0]-1,cur_pos[1]],[cur_pos[0]+1,cur_pos[1]],[cur_pos[0],cur_pos[1]-1],[cur_pos[0],cur_pos[1]+1]]
    for p in surround:
        if matrix[p[0]][p[1]]=='#':
            continue
        elif matrix[p[0]][p[1]]=='-' or matrix[p[0]][p[1]]=='e':
            if p not in queue:
                queue.append(p)
                origin.append(cur_pos)
    n+=1
def BackSearch(arr,a):
    for s in range(len(arr)-1,0,-1):
        if arr[s]==a:
            return s
    
path=[]
i=len(queue)-1
while True:
    path.append(queue[i])
    i=BackSearch(queue,origin[i])
    if i==None:
        break
path.append(bot)

path=path[::-1]

for i in range(0,len(path)-1):
    diff=[path[i+1][0]-path[i][0],path[i+1][1]-path[i][1]]
    if diff[0]<0:
        print('UP')
    elif diff[0]>0:
        print('DOWN')
    elif diff[1]<0:
        print('LEFT')
    elif diff[1]>0:
        print('RIGHT')
